# Grafos_projeto
Projeto de criação, manipulação e visualização de grafos. 
 

 
<img src="Imagens_readme/Horizontal-Vermelho-Logotipo-CIn-UFPE.png">
 

 

Universidade Federal de Pernambuco  

Centro de Informática - CIn  



Disciplina: Algoritmos e estruturas de dados 

Docente: Sergio Ricardo de Melo Queiroz 

Discente:  

Hyan Lucas Vieira da Silva 

Gustavo Diego da Silva 

 

 

Relatório do projeto: Grupo #2.1 

 

 

Recife, 27 de agosto de 2023
 

 

Contexto do problema 

O objetivo do programa é mostrar rapidamente uma maneira diferente de se avaliar uma viagem pelo mundo, ao invés de levar em conta a distância por estrada, mar ou ar e outras possíveis circunstâncias, ele oferece uma solução mais simples, ele pega a distância entre a capitais dos países em linha reta, sendo assim, uma maneira mais imparcial de se escolher um local para viajar, além disso, ele mostra o menor caminho passando por países ou não até chegar no destino desejado. A base de dados usada no projeto foi feita inteiramente pela dupla. A base de dados contém 94 países organizados por continentes, contém todas as possíveis ligações entre os países do mesmo continente e algumas ligações intercontinentais.  

 

Implementação 

Algoritmo utilizado. Utilizamos o algoritmo de Bellman-Ford para achar o menor caminho entre dois vértices e no caso países. 

 

Desenvolvimento. Primeiramente, elaboramos a ideia do projeto e em seguida partimos para a produção da nossa base de dados e por fim fizemos o programa solicitado. 

Além disso, em relação à divisão de funções, Hyan ficou responsável pela criação do banco de dados utilizando o (SEM, 2009), enquanto Gustavo se responsabilizou pelo programa, apesar disso, ambos participaram de ambas as partes por mais que houvesse um predomínio maior do responsável. 

 

Bibliotecas utilizadas. Nesse projeto, utilizamos as bibliotecas: Pandas, PIL, networkx, Matplotlib e tkinter. Pandas foi utilizado para a manipulação dos dados, retirando os dados da planilha e inserindo no código; networkx foi utilizado para passar os grafos feitos, anteriormente, para o matplolib; Matplotlib foi utilizado para a visualização dos grafos; tkinter foi utilizado para a criação da interface gráfica do programa; PIL foi utilizado para a inserção de imagem na interface gráfica. 

 

Conclusão O programa funciona seguinte forma: o usuário terá a opção de visualizar o grafo, feito com a base de dados, iniciando o código “visualização_de_dados” ou interagir com a interface gráfica, onde terá um menu para o usuário escolher quais dois países, ele deseja, para descobrir a distância mínima. 

 

Imagens da interface gráfica: 

 
<img src="Imagens_readme/Captura de tela 2023-08-27 172129.png">
 

Página inicial 

 <img src="Imagens_readme/Captura de tela 2023-08-27 172141.png">

Seleção dos países 

 
<img src="Imagens_readme/Captura de tela 2023-08-27 173907.png">
	 

Resultado da busca 

 <img src="Imagens_readme/Captura de tela 2023-08-27 173907.png">

Imagens da visualização gráfica: 

 
<img src="Imagens_readme/Captura de tela 2023-08-27 172011.png">
 

Grafo separado por cores que representam os continentes 

 
<img src="Imagens_readme/Captura de tela 2023-08-27 172051.png">
 

Grafo ampliado com as arestas coloridas (quanto mais verde menor é o peso e quanto mais vermelho maior o peso) 

 

 

 

 

 

 

 

 

 

 

 

 

 

 

 

 

 

 

Referências 

SEM, Nome. Distance from to. In: Distance from to: Distance Between Cities on Map. 0.0032. [S. l.], 2009. Disponível em: https://www.distancefromto.net/. Acesso em: 27 ago. 2023. 
