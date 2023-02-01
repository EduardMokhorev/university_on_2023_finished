#pragma once
#include "Dannie.cpp"

typedef
Node* pNode;

void newFile();
pNode openFile();
void saveFile(pNode& Head);
pNode CreatNode();
pNode Add(pNode& Head);
void vivodTop();
void vivodBot();
void vivodMid(int k, pNode Node);
void vivod(pNode& Head);
void poisk(pNode& Head);
void deleteNode(pNode& Head);
void EditNode(pNode& Head);
void sortStringFacult(pNode& Head);
void menu();