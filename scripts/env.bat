python -m venv env
source env/bin/activate    # Linux/macOS
env\Scripts\activate.bat   # Windows

pip install spacy medspacy pandas
python -m spacy download en_core_web_sm es_dep_news_trf
pip install spacy spacy-transformers