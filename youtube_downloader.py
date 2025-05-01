import os
import yt_dlp

DOWNLOAD_FOLDER = "audio_downloads"

def configurar_yt_dlp():
    """Configurações padrão para baixar apenas áudio"""
    return {
        'format': 'bestaudio/best',
        'postprocessors': [{
            'key': 'FFmpegExtractAudio',
            'preferredcodec': 'mp3',
            'preferredquality': '192',
        }],
        'outtmpl': os.path.join(DOWNLOAD_FOLDER, '%(title)s.%(ext)s'),
        'quiet': False,
        'no_warnings': True,
    }

def baixar_audio(url):
    """Baixa o áudio de um único link"""
    try:
        print(f"🔈 Baixando: {url}")
        with yt_dlp.YoutubeDL(configurar_yt_dlp()) as ydl:
            ydl.download([url])
        print("✅ Sucesso!")
    except Exception as e:
        print(f"❌ Erro no download de {url}: {e}")

def baixar_varios_audios(lista_links):
    """Baixa o áudio de vários links"""
    os.makedirs(DOWNLOAD_FOLDER, exist_ok=True)

    for url in lista_links:
        url = url.strip()
        if url and url.startswith(('http://', 'https://')):
            baixar_audio(url)
        else:
            print(f"⚠️ URL inválido ignorado: {url}")

def obter_links_manual():
    """Usuário cola os links manualmente"""
    print("\nCole todos os links desejados (1 por linha).")
    print("Quando terminar, digite 'FIM' e pressione Enter.\n")
    
    links = []
    while True:
        url = input("> ").strip()
        if url.lower() == 'fim':
            break
        links.append(url)
    
    return links

def obter_links_arquivo(nome_arquivo):
    """Lê links de um arquivo txt"""
    try:
        with open(nome_arquivo, 'r', encoding='utf-8') as f:
            links = f.readlines()
            return [link.strip() for link in links if link.strip()]
    except FileNotFoundError:
        print(f"❌ Arquivo '{nome_arquivo}' não encontrado.")
        return []

def main():
    print("\n🎵 YouTube Audio Downloader")
    print("=" * 50)

    escolha = input("\nDeseja carregar links de um arquivo TXT? (s/n): ").strip().lower()
    
    if escolha == 's':
        nome_arquivo = input("Digite o nome do arquivo (ex: links.txt): ").strip()
        links = obter_links_arquivo(nome_arquivo)
    else:
        links = obter_links_manual()

    if links:
        baixar_varios_audios(links)
    else:
        print("Nenhum link para baixar. Encerrando.")

if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        print("\n🛑 Programa encerrado pelo usuário.")
