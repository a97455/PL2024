import re
import sys

def markdown_to_html(markdown):
    # Cabeçalhos
    markdown = re.sub(r'^#\s+(.+)$', r'<h1>\1</h1>', markdown, flags=re.M)
    markdown = re.sub(r'^##\s+(.+)$', r'<h2>\1</h2>', markdown, flags=re.M)
    markdown = re.sub(r'^###\s+(.+)$', r'<h3>\1</h3>', markdown, flags=re.M)
    
    # Bold
    markdown = re.sub(r'\*\*(.*?)\*\*', r'<b>\1</b>', markdown)
    
    # Itálico
    markdown = re.sub(r'\*(.*?)\*', r'<i>\1</i>', markdown)

    # Imagem
    markdown = re.sub(r'!\[(.*?)\]\((.*?)\)', r'<img src="\2" alt="\1">', markdown)
    
    # Link
    markdown = re.sub(r'\[(.*?)\]\((.*?)\)', r'<a href="\2">\1</a>', markdown)

    # Parágrafos    
    markdown = re.sub(r'^\s*$', r'<p>', markdown, flags=re.M)
    markdown = re.sub(r'^(\S.*)\n\n', r'\1</p>\n\n', markdown, flags=re.M)
    markdown = markdown.replace('\n', ' ')
    
    return markdown

def convert_markdown_to_html_file(markdown_file_path):
    # Ler o conteúdo do arquivo Markdown
    with open(markdown_file_path, 'r', encoding='utf-8') as file:
        markdown_content = file.read()

    # Converter Markdown para HTML
    html_content = markdown_to_html(markdown_content)

    # Nome do arquivo HTML
    html_file_path = markdown_file_path.replace('.md', '.html')

    # Escrever o conteúdo HTML em um arquivo
    with open(html_file_path, 'w', encoding='utf-8') as file:
        file.write(html_content)


if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python markdown_to_html.py <caminho_para_arquivo_markdown>")
        sys.exit(1)

    convert_markdown_to_html_file(sys.argv[1])