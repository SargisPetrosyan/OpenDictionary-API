from fastapi import FastAPI

from services import (
    get_word_definitions,
    get_word_examples,
    get_word_synonyms,
    get_word_antonyms,
    get_word_usage_nots,
    get_word_related_words,
)


api = FastAPI()

@api.get("/")
def index():
    return {"Hello": "Word"}

@api.get('/{word}/definitions')
async def get_definitions(word:str):
    await get_word_definitions(word=word)

@api.get('/{word}/examples')
async def get_examples(word:str):
    await get_word_examples(word=word)

@api.get('/{word}/synonyms')
async def get_synonym(word:str):
    await get_word_synonyms(word=word)

@api.get('/{word}/antonyms')
async def get_antonym(word:str):
    await get_word_antonyms(word=word)

@api.get('/{word}/collections')
async def get_collection(word:str):
    await get_collection(word=word)

@api.get('/{word}/usage_nots')
async def get_usage_nots(word:str):
    await get_word_usage_nots(word=word)

@api.get('/{word}/related_words')
async def get_related_words(word:str):
    await get_word_related_words(word=word)

