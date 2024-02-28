<image src="https://www.gnu.org/graphics/gplv3-127x51.png">

**Nota:** Este programa foi desenvolvido com fins educacionais e para fins de aprendizado. O uso indevido do mesmo pode violar leis de privacidade e segurança. Utilize-o com responsabilidade.

# Quebrador de Senhas

Este é um pequeno e simples quebrador de senhas desenvolvido em Python, utilizando o método de força bruta. O programa é distribuído sob a licença GPL3. Certifique-se de ter recebido uma cópia da licença juntamente com o código-fonte. Caso contrário, você pode acessar a licença [aqui](https://www.gnu.org/licenses/gpl-3.0.en.html#license-text).

## Autor
Luiz Gabriel Magalhães Trindade

## Requisitos
- Python 3.x
- pyzipper

## Utilização
```bash
python quebrador_de_senhas.py arquivo.zip wordlist.txt
```

- `arquivo.zip`: O arquivo zip protegido por senha.
- `wordlist.txt`: O arquivo contendo a lista de senhas a serem testadas.

## Funcionamento
O programa divide a lista de senhas em quatro partes e executa quatro processos em paralelo para aumentar a eficiência.

## Instruções
1. Certifique-se de ter o Python 3.x instalado.
2. Instale a biblioteca `pyzipper` usando o seguinte comando:
    ```bash
    pip install pyzipper
    ```
3. Execute o programa fornecendo o arquivo zip e a wordlist como argumentos.

## Exemplo de Uso
```bash
python quebrador_de_senhas.py arquivo_protegido.zip lista_de_senhas.txt
```

## Observações
- O programa imprimirá a senha encontrada, o tempo total de execução e informações sobre o autor.
- Licenciado sob a [GPL3](https://www.gnu.org/licenses/gpl-3.0.en.html#license-text).

**Nota:** Este programa foi desenvolvido com fins educacionais e para fins de aprendizado. O uso indevido do mesmo pode violar leis de privacidade e segurança. Utilize-o com responsabilidade.