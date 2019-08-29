#!/usr/bin/python

# This file adjusts the block names of the style.css file for the production site  

fin = open("style.css", "rt")
data = fin.read()
# realizar as substituições para a versão de produção
data = data.replace('#block-block-6', '#block-block-16')
data = data.replace('#block-block-10', '#block-block-8')
data = data.replace('#block-block-15', '#block-block-9')
data = data.replace('#block-block-12', '#block-block-17')
data = data.replace('#block-block-20', '#block-block-18')

# Para reverter para a versão de teste, usar as seguintes substituições
# data = data.replace('#block-block-16', '#block-block-6')
# data = data.replace('#block-block-8', '#block-block-10')
# data = data.replace('#block-block-9', '#block-block-15')
# data = data.replace('#block-block-17', '#block-block-12')
# data = data.replace('#block-block-18', '#block-block-20')

fin.close()

fin = open("style.css", "wt")
fin.write(data)
fin.close()
