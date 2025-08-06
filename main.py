from fastapi import FastAPI

from services import (
    get_word_definitions,
    get_word_examples,
    get_word_synonyms,
    get_word_antonyms,
    get_word_usage_nots,
    get_word_related_words,
)


app = FastAPI()

@app.get('/{word}/definitions')
async def get_definitions(word:str):
    return await get_word_definitions(word=word)

@app.get('/{word}/examples')
async def get_examples(word:str):
    return await get_word_examples(word=word)

@app.get('/{word}/synonyms')
async def get_synonym(word:str):
    return await get_word_synonyms(word=word)

@app.get('/{word}/antonyms')
async def get_antonym(word:str):
    return await get_word_antonyms(word=word)

@app.get('/{word}/collections')
async def get_collection(word:str):
    return await get_collection(word=word)

@app.get('/{word}/usage_nots')
async def get_usage_nots(word:str):
    return await get_word_usage_nots(word=word)

@app.get('/{word}/related_words')
async def get_related_words(word:str):
    return await get_word_related_words(word=word)

