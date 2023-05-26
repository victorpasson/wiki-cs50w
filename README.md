# CS50W - Project 1 - Wiki

Repositório que contém o código para a solução do segundo projeto do curso CS50W - Web Programming. O objetivo principal é permitir que os usuários leiam, editem e criem novos conteúdos na plataforma. A aplicação foi construída com o Django framework.

[![Page Wiki Project](https://i.ibb.co/CVnmvBX/Opera-Instant-neo-2023-05-25-214413-wiki-cs50w-vercel-app.png)](www.youtube.com/watch?v=u0peDMCmqAE&t)

## Página do Projeto

O projeto foi disponibilizado para visualização por meio do [Vercel](https://wiki-cs50w.vercel.app).

Obs: Nessa plataforma, não será possível criar novas páginas nem editar as existentes devido a:

* Limitação de armazenamento da versão Free do Vercel;
* Por ser a versão Free, não é possível gravar novos arquivos, somente ler;
* Para uma aplicação assim seria melhor utilizar uma Base de Dados centralizada e não arquivos individuais em Markdown.

## Youtube Vídeo

Um breve vídeo de demonstração do resultado do projeto foi feito e hospedado no [YouTube](https://www.youtube.com/watch?v=u0peDMCmqAE&t).

## Especificações do projeto

1. **Páginas de Entrada** - visitando */wiki/TITLE*, onde *TITLE* é o título de uma entrada da enciclopédia, deve renderizar uma página que exibe o conteúdo para aquela entrada da enciclopédia.
    * Deve obter o conteúdo da entrada chamando a função apropriada do arquivo util.py;
    * Se a entrada requerida não existir, deve ser apresentado ao usuário uma página de erro indicando que a sua solicitação não foi encontrada;
    * Se a entrada existir, deve ser apresentado ao usuário uma página com o conteúdo daquela entrada. O título da página deve incluir o nome da entrada.

2. **Página Principal** - atualize *index.html*. Ao invés da página inicíal só apresentar uma lista com o nome de todas as páginas da enciclopédia, ao usuário deve ser habilitado clicar e ser redirecionado para a página solicitada.
    
3. **Pesquisa** - permita que o usuário escreva uma entrada de pesquisa para as páginas da enciclopédia.
    * Se a entrada corresponder ao nome de uma entrada da enciclopédia, o usuário deve ser redirecionado para aquela página; 
    * Se não corresponder ao nome de nenhuma entrada, o usuário deve ser redirecionado para uma página que exibe uma lista de todas páginas que possuem aquela palavra como substring. Por exemplo, se a pesquisa do usuário for *ython*, então *Python* deve aparecer no resultado da pesquisa;
    * Clicando no nome de qualquer um desses resultados de pesquisa, o usuário deve ser redirecionado para a página da enciclopédia daquele resultado.

4. **Nova Página** - clicando em "*Create New Page*” o usuário deve ser redirecionado para uma página onde pode criar uma nova página da enciclopédia.
    * Deve ser habilitado ao usuário: a) inserir um título para a página; b) inserir textos em Markdown, em uma *textarea*,  para o conteúdo da página;
    * Deve haver um botão para salvar as informações;
    * Quando a página é salva, se a entrada da enciclopédia já existir para aquele título, deve ser apresentado uma mensagem de erro ao usuário;
    * Caso contrário, a nova página será salva no diretório e o usuário será redirecionado a página criada.

5. **Editar Página** - Em cada página de resultado deve ser habilitado ao usuário clicar em um link que o leva para uma página onde pode editar o conteúdo Markdown daquela página em específico. Essa edição deve ser feita em uma *textarea*.
    * A *textarea* deve ser pré-preenchida com o conteúdo já existente para aquela página (isto é, o valor inicial de value já deve conter o conteúdo daquela página na *textarea*);
    * Ao usuário deve ser disponível um botão para salvar as mudanças feitas;
    * Assim que salvar, o usuário deve ser redirecionado para a página modificada.

6. **Página Aleatória** - clicando em “*Random Page*” o usuário deve ser levado para uma entrada aleatória da enciclopédia.
