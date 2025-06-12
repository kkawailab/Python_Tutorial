#!/usr/bin/env python3
"""
NumPyチュートリアルをHTMLに変換するスクリプト
"""

import re

def convert_markdown_to_html(md_content):
    """MarkdownをHTMLに変換"""
    
    # HTMLテンプレート
    html_template = """<!DOCTYPE html>
<html lang="ja">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>NumPy完全チュートリアル</title>
    <style>
        body {{
            font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, Arial, sans-serif;
            line-height: 1.6;
            color: #333;
            max-width: 900px;
            margin: 0 auto;
            padding: 20px;
            background-color: #f5f5f5;
        }}
        .container {{
            background-color: white;
            padding: 30px;
            border-radius: 10px;
            box-shadow: 0 2px 5px rgba(0,0,0,0.1);
        }}
        h1 {{
            color: #2c3e50;
            border-bottom: 3px solid #3498db;
            padding-bottom: 10px;
        }}
        h2 {{
            color: #2c3e50;
            margin-top: 40px;
            border-bottom: 2px solid #ecf0f1;
            padding-bottom: 5px;
        }}
        h3 {{
            color: #34495e;
            margin-top: 30px;
        }}
        code {{
            background-color: #f8f8f8;
            padding: 2px 5px;
            border-radius: 3px;
            font-family: 'Monaco', 'Consolas', monospace;
            font-size: 0.9em;
        }}
        pre {{
            background-color: #2c3e50;
            color: #ecf0f1;
            padding: 15px;
            border-radius: 5px;
            overflow-x: auto;
            line-height: 1.4;
        }}
        pre code {{
            background-color: transparent;
            padding: 0;
            color: #ecf0f1;
        }}
        .toc {{
            background-color: #ecf0f1;
            padding: 20px;
            border-radius: 5px;
            margin-bottom: 30px;
        }}
        .toc h2 {{
            margin-top: 0;
            color: #2c3e50;
        }}
        .toc ul {{
            list-style-type: none;
            padding-left: 0;
        }}
        .toc li {{
            margin: 5px 0;
        }}
        .toc a {{
            color: #3498db;
            text-decoration: none;
        }}
        .toc a:hover {{
            text-decoration: underline;
        }}
        .note {{
            background-color: #e8f4f8;
            border-left: 4px solid #3498db;
            padding: 10px 15px;
            margin: 20px 0;
            border-radius: 0 5px 5px 0;
        }}
        .warning {{
            background-color: #fcf8e3;
            border-left: 4px solid #f39c12;
            padding: 10px 15px;
            margin: 20px 0;
            border-radius: 0 5px 5px 0;
        }}
        table {{
            border-collapse: collapse;
            width: 100%;
            margin: 20px 0;
        }}
        th, td {{
            border: 1px solid #ddd;
            padding: 8px;
            text-align: left;
        }}
        th {{
            background-color: #3498db;
            color: white;
        }}
        tr:nth-child(even) {{
            background-color: #f2f2f2;
        }}
        .highlight {{
            background-color: #fff3cd;
            padding: 2px 4px;
            border-radius: 3px;
        }}
        .back-to-top {{
            position: fixed;
            bottom: 20px;
            right: 20px;
            background-color: #3498db;
            color: white;
            padding: 10px 15px;
            border-radius: 5px;
            text-decoration: none;
            display: none;
        }}
        .back-to-top:hover {{
            background-color: #2980b9;
        }}
        ul li {{
            margin: 5px 0;
        }}
        @media (max-width: 768px) {{
            body {{
                padding: 10px;
            }}
            .container {{
                padding: 20px;
            }}
            pre {{
                font-size: 0.85em;
            }}
        }}
    </style>
</head>
<body>
    <div class="container">
        {content}
    </div>
    <a href="#top" class="back-to-top">↑ トップへ</a>
    <script>
        // シンタックスハイライト用の簡単な処理
        document.addEventListener('DOMContentLoaded', function() {{
            // Python キーワードのハイライト
            const keywords = ['import', 'from', 'def', 'class', 'return', 'if', 'else', 'elif', 
                            'for', 'while', 'in', 'True', 'False', 'None', 'and', 'or', 'not',
                            'try', 'except', 'finally', 'with', 'as', 'pass', 'break', 'continue',
                            'print', 'np', 'numpy', 'array', 'shape', 'dtype'];
            
            const codeBlocks = document.querySelectorAll('pre code');
            codeBlocks.forEach(block => {{
                let html = block.innerHTML;
                
                // 文字列をハイライト（シングルクォートとダブルクォート）
                html = html.replace(/('[^']*'|"[^"]*")/g, '<span style="color: #e74c3c;">$1</span>');
                
                // 数値をハイライト
                html = html.replace(/\b(\d+\.?\d*)\b/g, '<span style="color: #e67e22;">$1</span>');
                
                // コメントをハイライト
                html = html.replace(/(#[^\n]*)/g, '<span style="color: #95a5a6;">$1</span>');
                
                // キーワードをハイライト
                keywords.forEach(keyword => {{
                    const regex = new RegExp('\\b(' + keyword + ')\\b', 'g');
                    html = html.replace(regex, '<span style="color: #3498db; font-weight: bold;">$1</span>');
                }});
                
                block.innerHTML = html;
            }});
            
            // スクロールでトップへ戻るボタンの表示/非表示
            const backToTop = document.querySelector('.back-to-top');
            window.addEventListener('scroll', function() {{
                if (window.pageYOffset > 300) {{
                    backToTop.style.display = 'block';
                }} else {{
                    backToTop.style.display = 'none';
                }}
            }});
        }});
    </script>
</body>
</html>"""
    
    # コードブロックを一時的に保護
    code_blocks = []
    def save_code_block(match):
        code_blocks.append(match.group(0))
        return f"__CODE_BLOCK_{len(code_blocks)-1}__"
    
    # ```で囲まれたコードブロックを保護
    html = re.sub(r'```[\s\S]*?```', save_code_block, md_content)
    
    # 見出しの変換
    html = re.sub(r'^### (.*?)$', r'<h3>\1</h3>', html, flags=re.MULTILINE)
    html = re.sub(r'^## (.*?)$', r'<h2>\1</h2>', html, flags=re.MULTILINE)
    html = re.sub(r'^# (.*?)$', r'<h1>\1</h1>', html, flags=re.MULTILINE)
    
    # リストの変換
    html = re.sub(r'^\* (.*?)$', r'<li>\1</li>', html, flags=re.MULTILINE)
    html = re.sub(r'^\- (.*?)$', r'<li>\1</li>', html, flags=re.MULTILINE)
    html = re.sub(r'^\d+\. (.*?)$', r'<li>\1</li>', html, flags=re.MULTILINE)
    
    # 連続するリストアイテムをulタグで囲む
    html = re.sub(r'(<li>.*?</li>\n?)+', lambda m: '<ul>\n' + m.group(0) + '</ul>\n', html)
    
    # 太字と斜体
    html = re.sub(r'\*\*\*(.*?)\*\*\*', r'<strong><em>\1</em></strong>', html)
    html = re.sub(r'\*\*(.*?)\*\*', r'<strong>\1</strong>', html)
    html = re.sub(r'\*(.*?)\*', r'<em>\1</em>', html)
    
    # インラインコード
    html = re.sub(r'`([^`]+)`', r'<code>\1</code>', html)
    
    # リンク
    html = re.sub(r'\[([^\]]+)\]\(([^)]+)\)', r'<a href="\2">\1</a>', html)
    
    # 改行を<br>に変換（ただし、タグの後は除く）
    html = re.sub(r'(?<!>)\n(?!<)', '<br>\n', html)
    
    # 段落の処理
    html = re.sub(r'\n\n+', '</p>\n<p>', html)
    html = '<p>' + html + '</p>'
    
    # 不要な<p>タグを削除
    html = re.sub(r'<p>(<h[1-6]>)', r'\1', html)
    html = re.sub(r'(</h[1-6]>)</p>', r'\1', html)
    html = re.sub(r'<p>(<ul>)', r'\1', html)
    html = re.sub(r'(</ul>)</p>', r'\1', html)
    html = re.sub(r'<p></p>', '', html)
    
    # コードブロックを復元
    for i, code_block in enumerate(code_blocks):
        # ```python などの言語指定を削除
        code_content = re.sub(r'^```\w*\n', '', code_block)
        code_content = re.sub(r'\n```$', '', code_content)
        # HTMLエスケープ
        code_content = code_content.replace('&', '&amp;')
        code_content = code_content.replace('<', '&lt;')
        code_content = code_content.replace('>', '&gt;')
        html = html.replace(f"__CODE_BLOCK_{i}__", f'<pre><code>{code_content}</code></pre>')
    
    # 目次のリンクを修正
    def make_anchor(title):
        # 日本語を含むアンカーリンクの生成
        anchor = re.sub(r'[^\w\s-]', '', title.lower())
        anchor = re.sub(r'[-\s]+', '-', anchor)
        return anchor
    
    # 見出しにIDを追加
    def add_heading_id(match):
        level = match.group(1)
        title = match.group(2)
        anchor = make_anchor(title)
        # 日本語の場合は連番を使用
        if not anchor or anchor == '-':
            anchor = f"section-{add_heading_id.counter}"
            add_heading_id.counter += 1
        return f'<h{level} id="{anchor}">{title}</h{level}>'
    
    add_heading_id.counter = 1
    html = re.sub(r'<h([1-6])>(.*?)</h\1>', add_heading_id, html)
    
    # HTMLテンプレートに組み込む
    final_html = html_template.format(content=html)
    
    return final_html

def main():
    # MarkdownファイルをHTMLに変換
    try:
        with open('NumPy_Tutorial_Complete.md', 'r', encoding='utf-8') as f:
            markdown_content = f.read()
        
        html_content = convert_markdown_to_html(markdown_content)
        
        with open('NumPy_Tutorial_Complete.html', 'w', encoding='utf-8') as f:
            f.write(html_content)
        
        print("NumPy_Tutorial_Complete.html を生成しました。")
        
    except FileNotFoundError:
        print("エラー: NumPy_Tutorial_Complete.md が見つかりません。")
    except Exception as e:
        print(f"エラーが発生しました: {e}")

if __name__ == "__main__":
    main()