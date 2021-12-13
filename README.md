<h1 align='center'>
<img src="https://github.com/liliangisellyps/projeto-final-lccv/blob/master/front-end-lccv/src/assets/logo-lccv.png?raw=true" height='90'>
</h1>
<h1 align='center'>Curso de Formação Full Stack Júnior</h1>

#
# 💻 Descrição do desafio
Projeto de uma aplicação full-stack web para a empresa Sumé Software, inicialmente com a tela de cadastro de patrimônios. Curso seletivo promovido pelo LCCV - Laboratório de Computação Científica e Visualização.

#
# 💻 Front-end

## 📚 Tecnologias
- HTML, SCSS e Bootstrap 
- TypeScript
- Angular

## 🎉 Telas Front-End

<p align='center'>
  <img src="https://github.com/liliangisellyps/projeto-final-lccv/blob/master/img/lccv-1.png?raw=true" width="300px">
  <img src="https://github.com/liliangisellyps/projeto-final-lccv/blob/master/img/lccv-2.png?raw=true" width="300px">
</p>


<p align='center'>
  <img src="https://github.com/liliangisellyps/projeto-final-lccv/blob/master/img/lccv-3.png?raw=true" width="300px">
  <img src="https://github.com/liliangisellyps/projeto-final-lccv/blob/master/img/lccv-4.png?raw=true" width="300px">
</p>

<p align='center'>
  <img src="https://github.com/liliangisellyps/projeto-final-lccv/blob/master/img/lccv-5.png?raw=true" width="300px">
  <img src="https://github.com/liliangisellyps/projeto-final-lccv/blob/master/img/lccv-6.png?raw=true" width="300px">
</p>

## 👩‍💻 Execução:
    cd front-end-lccv
    ng serve

    Acessar o link: http://localhost:4200/cadastrar

## 👩‍💻 Rotas:

    http://localhost:4200/cadastrar
    http://localhost:4200/listar
    http://localhost:4200/home
## 👩‍💻 Relatório:
- Apesar de nunca ter mexido com angular e bootstrap, consegui implementar as telas de front-end sem muitas dificuldades tomando como base as aulas, as documentações e a bagagem de conhecimento anterior com outros frameworks. Apesar da não ter achado complexo, demandou bastante tempo e pesquisa.
- Tive dificuldade com os componentes accordion e modal, provavelmente advindos de algum problema no jQuery. Contornei esse problema usando os componentes equivalentes do ``ngx bootstrap``.
- Os dados dos formulários estão estáticos, não estão sendo salvos nem enviados pois não houve integração com o back-end. 
- A página de listagem dos bens não foi feita pois apesar de ter o layout disponível não foi requerida no backlog e não sobrou tempo para implementá-la, priorizei colocar os esforços no back-end.

#
# 💻 Back-end

## 📚 Tecnologias
- Python
- Docker
- Django
- Django Rest Framework


## 👩‍💻 Execução:
    docker-compose build
    docker-compose up

    Acessar o link: http://localhost:4200/

## 👩‍💻 Relatório:
- Nunca havia mexido com back-end e, portanto, encontrei mais dificuldades. No entanto, não foi até a implementação do último módulo (Django Rest Framework) que elas apareceram. 
- Implementei os models, as migrations, signals e actions sem problemas. Consegui mexer no django admin através do ``env`` e do Docker, criando o banco de dados com sucesso. 
- No último módulo, após criar alguns modelos de serializer, views e urls, a aplicação começou a dar problema e não reconhecer a importação do "rest_framework",Ela parou de funcionar e apareceram mais erros.
- Apesar de muito procurar a solução e até mesmo voltar à versão anterior que estava sem falhas (perdendo assim o que havia feito com o django rest), não consegui descobrir a causa dos erros e, portanto, também não consegui solucioná-los. 

#
# 💻 Conclusão:

Tive uma boa experiência e foi um curso bastante proveitoso, através dele tive a oportunidade de aprender tecnologias que ainda não havia mexido. As aulas foram boas e didáticas, obtive um grande aproveitamento. Infelizmente surgiram imprevistos ao decorrer do desenvolvimento e não tive tempo o suficiente para avançar com o projeto tanto quanto desejava. 
