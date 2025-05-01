
# 🎵 YouTube Audio Downloader

Este é um script Python que utiliza a biblioteca `yt_dlp` para baixar áudios em MP3 de vídeos do YouTube (ou de outras plataformas suportadas), com foco em simplicidade e funcionalidade.

---

## ✅ Funcionalidades

- Baixa o áudio no formato `.mp3` com qualidade 192kbps.
- Aceita um ou vários links.
- Links podem ser inseridos manualmente ou carregados de um arquivo `.txt`.
- Cria automaticamente a pasta `audio_downloads` para armazenar os arquivos.

---

## 🛠️ Requisitos

- Python 3.7 ou superior  
- `yt-dlp`  
- `ffmpeg` (necessário para conversão para MP3)

### Instalação das dependências

```bash
pip install yt-dlp
```

#### No Linux:

```bash
sudo apt install ffmpeg
```

#### No Windows:
## Obs: caso não queira baixar, tem no proprio repositorio um zip, basta descompactar e utilizar ele mesmo, lembre de colocar nas bariaveis de ambiente bin
1. Baixe o ffmpeg em: [https://ffmpeg.org/download.html](https://ffmpeg.org/download.html)
2. Extraia o conteúdo.
3. Adicione o caminho da pasta `bin` à variável de ambiente `PATH`.

---

## ▶️ Como usar

1. Clone ou baixe este repositório.
2. Execute o script:

```bash
python nome_do_arquivo.py
```

3. O programa perguntará se deseja carregar os links de um arquivo `.txt`.
   - Se sim, digite o nome do arquivo (ex: `links.txt`), que deve conter um link por linha.
   - Se não, cole os links manualmente no terminal e digite `FIM` para finalizar.

---

## 📁 Estrutura de pastas

```
📂 audio_downloads/      ← Arquivos MP3 baixados são salvos aqui
📄 nome_do_arquivo.py    ← Script principal
📄 links.txt             ← (opcional) Arquivo de entrada com URLs
```

---

## 📌 Exemplo de `links.txt`

```
https://www.youtube.com/watch?v=abc123
https://www.youtube.com/watch?v=xyz456
```

---

## ⚠️ Observações

- O script ignora links inválidos ou vazios.
- Pode ser interrompido a qualquer momento com `Ctrl + C`.
