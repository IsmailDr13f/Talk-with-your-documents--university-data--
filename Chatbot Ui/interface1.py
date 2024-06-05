import streamlit as st
from datetime import datetime
from pymongo import MongoClient 
import requests
import json
from flask import jsonify
st.set_page_config(page_title="HERCULES",
                   page_icon="poseidon_1297826.png",
                   )

# Connexion à la base de données MongoDB
client = MongoClient("mongodb://localhost:27017/")
db = client["discussions"]
collections = db.list_collection_names()
collections.sort(reverse=True)

# Titre de l'application
st.markdown("<h1 style='text-align: center;'>HERCULES</h1>", unsafe_allow_html=True)

# Initialisation de l'historique des discussions
if 'discussions' not in st.session_state:
    st.session_state['discussions'] = {}


if 'save' not in st.session_state:
    st.session_state.save = 0


# Entrée utilisateur pour la requête
user_query = st.chat_input("Entrez votre question ", max_chars=400)

#initialisation de l'id de discussion
if user_query and st.session_state.save == 0:
    st.session_state.discussion_id = "Discussion_"+datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    st.session_state['discussions'][st.session_state.discussion_id] = []
    st.session_state.save = 1

if 'model' not in st.session_state:
    st.session_state.model = None

if user_query:

    # Envoyer le user_query à l'API Flask
    #api_url = 'http://127.0.0.1:5000/process_query'
    #data = {'user_query': user_query}
    #headers = {'Content-type': 'application/json', 'Accept': 'text/plain'}
    #res = requests.post(api_url,data=json.dumps(data), headers=headers)

    def send_query(query,model_name="mistral"):
        url = 'http://127.0.0.1:5000/process'
        #payload = {'query': query}
        payload = {'query': query, 'model_name': model_name}
        response = requests.post(url, json=payload)
        if response.status_code == 200:
            return response.json().get('result', '')
        else:
            return None
    
    

    # Récupérer la réponse de l'API
    assistant_response = send_query(user_query, st.session_state.model )
    print(f"Result: {assistant_response}")

    # Ajouter le message de l'utilisateur à l'historique des messages          
    st.session_state['discussions'][list(st.session_state['discussions'].keys())[0]].append({'role': 'user', 'content': user_query, 'time':datetime.now().strftime("%Y-%m-%d %H:%M:%S")})
    
    # Exemple de traitement de la requête utilisateur (à remplacer par votre propre logique)
    #response = f"Vous avez demandé : {user_query}"
    response = assistant_response
    # Ajouter la réponse du système à l'historique des messages
    st.session_state['discussions'][list(st.session_state['discussions'].keys())[0]].append({'role': 'assistant', 'content': response, 'time':datetime.now().strftime("%Y-%m-%d %H:%M:%S")})

    print(st.session_state['discussions'])
    st.rerun()


def new_disc():
    if not user_query and st.session_state['discussions'] == {}:
    
        st.markdown("<h5 style='text-align: center;'>v_1.0.0</h5>", unsafe_allow_html=True)

        col1, col2, col3 = st.columns(3)
        with col1:
                con1 = st.container(border=1)
                con1.markdown("👨‍💼 Support administratif et équipes professorales")

        with col2:
                con2 = st.container(border=1)
                con2.markdown("📒  Programmes et cours à la FSTT")

        with col3:
                con3 = st.container(border=1)
                con3.markdown("🌐 Informations externes\nà la FSTT")

        st.caption("⚠️Hercules peut prendre quelques secondes ou minutes pour générer la réponse. S'il vous plaît, vérifiez la qualité des réponses générées.")

    # Afficher l'historique des messages de la discussion
    if st.session_state['discussions'].keys() != [] :
        for k,v in st.session_state['discussions'].items():
            st.write(k)
            for message in v:
                with st.chat_message(message['role']):
                    st.write(message['content'])

new_disc()


# Using "with" notation
with st.sidebar:
    c1, c2, c3 = st.columns(3)
    with c1:
            st.write("")

    with c2:
            st.image("poseidon_1297826.png")

    with c3:
            st.write("")
    
    if st.button("Nouvelle Discussion",use_container_width=True):
        if st.session_state.save == 1:
            st.session_state['discussions'] = {}
        st.session_state.save = 0
        st.rerun()

    @st.experimental_dialog("Enregistrement!")
    def save_dialog():
        st.write("Votre Conversassion à été enregistrée avec succes!")
        if st.button("OK"):
            st.rerun()
    if st.button("Enregistrer la conversation",use_container_width=True,type="primary"):
        if st.session_state.save == 1:
            if list(st.session_state['discussions'].keys())[0] not in collections:
                collection = db[list(st.session_state['discussions'].keys())[0]]
                collection.insert_many(st.session_state['discussions'][list(st.session_state['discussions'].keys())[0]])
            else:
                try:
                    # Supprimer la collection si elle existe
                    db.drop_collection(list(st.session_state['discussions'].keys())[0])
                except Exception as e:
                    print(e)
                                            
                try:
                    # Créer une nouvelle collection et insérer des documents
                    collection = db[list(st.session_state['discussions'].keys())[0]]
                    collection.insert_many(st.session_state['discussions'][list(st.session_state['discussions'].keys())[0]])
                except Exception as e:
                    print(e)
        save_dialog()
        

    st.markdown("### Methodes & modéles")
    add_radio = st.radio(
        "Choisir une method",
        ("RAG", "Fine-tuning")
    )

    @st.experimental_dialog("Attention!")
    def show_dialog():
        st.write("La méthode the Fine-tuning est en cours de réalisation,Merci pour votre compréhension.")
        
    if add_radio == "RAG":
        add_selectbox = st.sidebar.selectbox(
            "Choisir un modele de LLM",
            ("mistral", "llama2", "llama3","gemma")
        )
        st.session_state.model = add_selectbox
        print("Model:",add_selectbox)
    else:
        #add_selectbox = st.sidebar.selectbox(
        #    "Choisir un modele de LLM",
        #    ("NousResearch/Llama-2-7b-chat-hf",)
        #)
        show_dialog()
    st.markdown("### Historique des discussions")
    disc=st.container(border=1,height=250)
    with disc:
        print(collections)
        for coction in collections:
            if st.button(coction, use_container_width=True):
                st.session_state['discussions'] = {}
                colls_date = []
                collectio = db[coction]
                cursor = collectio.find()
                for document in cursor:
                    rest_of_document = {k: v for k, v in list(document.items())[1:]}
                    colls_date.append(rest_of_document)
                st.session_state['discussions'][coction] = colls_date
                st.session_state.save = 1
                st.rerun()

    st.caption("v1.0.0_hercules")
