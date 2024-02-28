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

# Escolha da Licença GPL3

A escolha da Licença Pública Geral GNU (GPL3) para o quebrador de senhas desenvolvido é estratégica e alinhada com as características do programa. A GPL3 é uma licença de software livre que oferece diversas vantagens, especialmente para programas que se baseiam em distribuição e colaboração aberta. Aqui estão alguns motivos para a escolha da GPL3:

## 1. **Compatibilidade com Software Livre:**
   A GPL3 é uma licença que promove a liberdade de software. Ela garante que o código-fonte seja acessível a todos os usuários, permitindo que eles visualizem, modifiquem e distribuam as versões modificadas. Isso está alinhado com os princípios do movimento de software livre.

## 2. **Proteção da Liberdade do Usuário:**
   A GPL3 assegura que qualquer pessoa que receba uma cópia do programa também tenha acesso ao código-fonte. Isso protege a liberdade do usuário, garantindo que ele tenha controle sobre o software instalado em seus sistemas.

## 3. **Colaboração Aberta:**
   Ao escolher a GPL3, você incentiva a colaboração aberta. Outros desenvolvedores podem contribuir para o projeto, aprimorando-o e beneficiando a comunidade como um todo. A GPL3 exige que as modificações também sejam distribuídas sob os mesmos termos, garantindo um ciclo de colaboração contínua.

## 4. **Prevenção contra Uso Proprietário:**
   A GPL3 impede que o código seja utilizado em projetos proprietários, garantindo que as melhorias e extensões permaneçam disponíveis para a comunidade. Isso evita que o software seja fechado e monopolizado.

## 5. **Transparência e Confiança:**
   A GPL3 promove a transparência ao fornecer o código-fonte junto com o software. Isso constrói confiança na comunidade de usuários, pois eles podem verificar como o programa funciona e tomar decisões informadas sobre seu uso.

Em resumo, a escolha da GPL3 reflete o compromisso com os princípios do software livre, a promoção da colaboração aberta e a garantia da liberdade do usuário. Essa licença cria um ambiente propício para o desenvolvimento comunitário e a disseminação do conhecimento.

**Nota:** Este programa foi desenvolvido com fins educacionais e para fins de aprendizado. O uso indevido do mesmo pode violar leis de privacidade e segurança. Utilize-o com responsabilidade.