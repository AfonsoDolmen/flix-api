import openai


openai.api_key = client = 'SUA-CHAVE-API'

# Gera resumo com IA
def generate_resume(title, genre, release_date) -> str:
    # Prompt
    prompt = f'''
    Você é um ótimo apreciador de filmes, e deve gerar um resumo do filme
    {title} do gênero {genre} e do ano de {release_date.year}. O resumo deve até
    500 caracteres.
    '''

    completion = openai.chat.completions.create(
        model='gpt-4o-mini',
        store=False,
        messages=[
            {
                'role': 'assistant',
                'content': prompt,
            }
        ]
    )

    # Retorna o conteúdo gerado pela IA
    return completion.choices[0].message.content
