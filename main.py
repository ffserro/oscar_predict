import streamlit as st
import pickle as pkl
import pandas as pd

st.title('Previsão do Oscar!')

proba_model = pkl.load(open('./ensemble_proba_model.pkl', 'rb'))


with st.form('Movie_production'):

    marketing_expense = st.number_input('Quanto foi o gasto total com marketing do filme?')

    production_expense = st.number_input('Quanto foi o gasto total da produção?')

    multiplex_coverage = st.number_input('Quanto foi a cobertura média Multiplex?')

    budget = st.number_input('Quanto foi o orçamento total do filme?')

    movie_length = st.number_input('Quanto tempo de duração tem o filme?')

    lead_actor_rating = st.number_input('Qual é a avaliação do ator principal?')

    lead_actress_rating = st.number_input('Qual é a avaliação da atriz principal?')

    director_rating = st.number_input('Qual é a avaliação do diretor?')

    producer_rating = st.number_input('Qual é a avaliação do produtor?')

    critic_rating = st.number_input('Qual é a avaliação dada pelos críticos?')

    trailer_views = st.number_input('Qual á o número de visualizações do trailer?')

    time_taken = st.number_input('Quanto tempo o filme levou para ser gravado?')

    twitter_hashtags = st.number_input('Quantas menções no Twitter o filme teve?')

    genre = st.selectbox('Qual é o gênero do filme?', options = ['Suspense', 'Drama', 'Comédia', 'Ação'])

    genre = ['Suspense', 'Drama', 'Comédia', 'Ação'].index(genre)

    avg_age_actors = st.number_input('Qaul é a idade média dos atores?')

    num_multiplex = st.number_input('Qual é o número de multiplexes?')

    collection = st.number_input('Qual é a coleção?')

    enviar = st.form_submit_button('Enviar')

if enviar:
    entry = pd.DataFrame({
        'Marketing expense' : [marketing_expense], 
        'Production expense' : [production_expense], 
        'Multiplex coverage' : [multiplex_coverage],
        'Budget' : [budget], 
        'Movie_length' : [movie_length], 
        'Lead_ Actor_Rating' : [lead_actor_rating], 
        'Lead_Actress_rating' : [lead_actress_rating],
        'Director_rating' : [director_rating], 
        'Producer_rating' : [producer_rating], 
        'Critic_rating' : [critic_rating], 
        'Trailer_views' : [trailer_views],
        'Time_taken' : [time_taken], 
        'Twitter_hastags' : [twitter_hashtags], 
        'Genre' : [genre], 
        'Avg_age_actors' : [avg_age_actors],
        'Num_multiplex' : [num_multiplex], 
        'Collection' : [collection]})

    st.write(proba_model.predict_proba(entry))

