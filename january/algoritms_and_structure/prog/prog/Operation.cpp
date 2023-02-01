#define _CRT_SECURE_NO_WARNINGS

#include <Windows.h>
#include <stdio.h>
#include "Dannie.cpp"

typedef
Node* pNode;
char file[200];

void newFile()
{
	FILE* F;  //���������� ���������� �� ����
	printf("������� ��� �����:"); //����� ������� �� �����
	scanf("%s", file); //������� ��� �����
	fflush(stdin); //�������� �����
	strcat(file, ".zap"); //�������� ���������� � �����
	F = fopen(file, "wb"); //������� ���� ��� ������
	fclose(F); //������� ����
	F = NULL;
}

pNode openFile()
{
	pNode  Head = NULL; //��������� �� ������ ������ NULL
	FILE* F; //��������� �� ����
	printf("������� ��� �����: "); //��� ����� �����
	scanf("%s", file); //������� ���
	fflush(stdin); //��������� �����
	strcat(file, ".zap"); //�������� � ����� ����������
	F = fopen(file, "rb");  //������� ���� ��� ������ ������
	if (F == NULL) printf("���� %s �� ������ ��� ����\n", file); //���� ���� �� ������ ������ ������
	else
	{
		Sorevnovanija sorevnovanija; //���������� ���� ������
		pNode NewNode = new Node; //������ ����� ����
		while (fread(&sorevnovanija, sizeof(Sorevnovanija), 1, F) != 0) //���� �� ����� �����, ��������� � ���������� ������
		{
			if (Head == NULL) { //���� ������ ��� ���
				Head = NewNode; //������� ������ ������ �������� �������
				NewNode->Next = NULL; //���������� �������� ���
				strcpy(NewNode->sorevnovanija.facultet, sorevnovanija.facultet); //������� ��������
				NewNode->sorevnovanija.countStud = sorevnovanija.countStud; //������� �������� ���������� ���������
				NewNode->sorevnovanija.srBall = sorevnovanija.srBall; //������� �������� ����
				NewNode->sorevnovanija.otl = sorevnovanija.otl; //������� ����������
				NewNode->sorevnovanija.dv = sorevnovanija.dv; //������� ����������
			}
			else //�����
			{
				pNode q = new Node; //������� ����
				strcpy(q->sorevnovanija.facultet, sorevnovanija.facultet); //������� ��������
				q->sorevnovanija.countStud = sorevnovanija.countStud; //������� ����������
				q->sorevnovanija.srBall = sorevnovanija.srBall; //������� ������� ����
				q->sorevnovanija.otl = sorevnovanija.otl; //����������
				q->sorevnovanija.dv = sorevnovanija.dv;  //����������
				q->Next = NULL; //��������� ������� �� ��� NULL
				NewNode->Next = q; //�������� ��������� � �����
				NewNode = NewNode->Next; //������� �� ���������� �������
			}
		}
		fclose(F); //������� ����
	}
	return Head; //������� ��������� �� ������ ������
}

void saveFile(pNode& Head)
{
	pNode Node; //��������� �� ������

	FILE* F; //��������� �� ����
	if (strcmp(file, "") == 0) //���� ���� ��� �� ������
	{
		printf("������� ��� �����: ");
		scanf("%s", file); //������� ��� �����
		strcat(file, ".zap"); //�������� � ���� ����������
	}
	F = fopen(file, "wb"); //������� ��� ������
	if (F == NULL) printf("���� %s �� ������ ��� ����\n", file); else //��� ���� �� ��������, ������ ������, �����
	{
		Node = Head; //��������� ��������� �� ������ ������
		Sorevnovanija sorevnovanija; //���������� ���� ������
		while (Node != NULL) { //���� �� ����� ������
			sorevnovanija = Node->sorevnovanija; //���������� ������ � ����������
			fwrite(&sorevnovanija, sizeof(sorevnovanija), 1, F); //��������� ������ � ����
			Node = Node->Next; //������� �� ��������� ������
		}
	}
	fclose(F); //������� ����
}


pNode CreatNode() {
	pNode NewNode = new Node; //������� ����
	int q; //������������� ����������
	Sorevnovanija temp; //��������� ���������� ���� ���������
	printf("������� ���������: "); //������ ����� ������
	getchar(); //��������� ����� \n � ������
	gets_s(temp.facultet); //������� ��������� (����� � ���������)
	printf("������� ���������� ���������: ");
	scanf("%d", &temp.countStud);//������� ���������� %d - ����� ����� 
	printf("������� ������� ����: ");
	scanf("%lf", &temp.srBall); //%lf - ����� ���� double
	printf("������� ���������� ����������:");
	scanf("%d", &temp.otl); //������� ����������
	printf("������� ���������� ����������:");
	scanf("%d", &temp.dv); //������� ����������
	NewNode->sorevnovanija = temp; //�������� ������ � ������
	NewNode->Next = NULL; //��������� �������
	return(NewNode); //������� ��������� �� ��������� �������
}


pNode Add(pNode& Head)
{
	pNode p = NULL, q = NULL; //��������� �� ������
	pNode NewNode = new Node; //������� �����
	int r, l, i; //������������� ����������
	q = Head; //��������� ������ �����
		NewNode = CreatNode(); //������� ������� �������� ��������
		NewNode->Next = Head; //�������� ������ �� ������
		Head = NewNode; //��������� ������ ������� �������
	return(Head); //������� ������
}


void vivodTop()
{
	printf("_____________________________________________________________________________________________________________________\n");
	printf("|  �  |         ������������ ����������         | ���������� ��������� | ������� ���� |   ���������   |  ���������  |\n");
	printf("| �/� |                                         |                      |              |               |             |\n");
} //������ ����� �������
void vivodBot()
{
	printf("|_____|_________________________________________|______________________|______________|_______________|_____________|\n");

} //������ ������� �������
void vivodMid(int k, pNode Node)
{
	//������� ������� , %����� ���������� ������� ������� ��������
	printf("|%5d|%41s|%22d|%14.2lf|%15d|%13d|\n", k, Node->sorevnovanija.facultet, Node->sorevnovanija.countStud, Node->sorevnovanija.srBall, Node->sorevnovanija.otl, Node->sorevnovanija.dv);
}
void vivod(pNode& Head) {
	pNode Node; //��������� �� ������
	vivodTop(); //������� �����
	Node = Head; //��������� ������
	int k = 1;
	while (Node != NULL) { //���� ������ �� ����
		vivodBot(); //������� ������
		vivodMid(k, Node); //����� ��������
		Node = Node->Next; //������� � ���������� ��������
		k++; //����������� ����� �� �������
	}
	vivodBot(); //����� �������
}


void deleteNode(pNode& Head)
{
	pNode q = Head, OlmestNode; //��������� �� ������ 
	int l, i; //��������� ����������
	vivod(Head); //����� ������� ������ ���� �������
	printf("������� ����� ���������� ��������:");
	scanf("%d", &l); //���� ������ �� ������� ��������� ������
	i = 1; //�������� ������� � ������� ��� ������������
	while (i != l) { //���� �� ������� ������ ���������� �������
		q = q->Next; //������� � ���������
		i++; //��������� �������
	}
	OlmestNode = q; //��������� ����� ������� ��������
	q = Head; //��������� ������ ������
	if (Head == OlmestNode) //���� ��������� ������ ������� 
		Head = OlmestNode->Next; //���������� ������� ��������� �� ���
	else { 
		while (q->Next != OlmestNode) //����� ����� ������ �������
			q = q->Next; //������� � ���������
		if (q == NULL) return; //���� �� ������, �� ����� 
		q = q->Next = OlmestNode->Next; //����� �������������� ������
	}
	delete OlmestNode; //������� �������
}

void EditNode(pNode& Head)
{
	int l, k, i;
	pNode Node;
	Node = Head;
	system("cls");
	vivod(Head);
	if (Head != NULL) {
		printf("������� ����� ������ ��� ���������:");
		scanf("%d", &l);
		printf("������� ����� ���� ��� ���������:\n1 - ������������ ����������\n2 - ���������� ���������\n3 - ������� ����\n4 - ���������� ����������\n5 - ���������� ����������\n");
		scanf("%d", &k);
		i = 0;
		while (Node != NULL) { //���� �� ������� ������ ������
			i++;
			if (i == l) break; //���� �����, �� ����� �� �����
			Node = Node->Next; //����� ������� ������
		}
		if (Node != NULL) {
			if (k == 1) { //���� ������� ������ ����
				printf("������� ������������ ����������:");
				getchar(); //������� ������ ������� �� �������
				gets_s(Node->sorevnovanija.facultet); //������� ����� ������������
			}
			if (k == 2) {//���� ������� ������ ����
				printf("������� ���������� ���������:");
				fflush(stdin); //�������� �����
				scanf("%d", &Node->sorevnovanija.countStud); //������� ���������� ���������
			}
			if (k == 3) { //���� ������� ������ ����
				printf("������� ������� ����:");
				fflush(stdin); //�������� �����
				scanf("%lf", &Node->sorevnovanija.srBall);//������� ������� ���� ���������
			}
			if (k == 4) { //���� ������� ��������� ����
				printf("������� ���������� ����������:");
				fflush(stdin);//�������� �����
				scanf("%d", &Node->sorevnovanija.otl); //������� ���������� ���������� 
			}
			if (k == 5) {//���� ������� ����� ����
				printf("������� ���������� ����������:");
				fflush(stdin); //�������� �����
				scanf("%d", &Node->sorevnovanija.dv); //������� ����� �������
			}
		}
	}
}


void sortStringFacult(pNode& Head){
	/* C��������� ��������� �� �������� ���������� */
	pNode Node; //��������� �� ������
	Sorevnovanija temp; //��������� ���������� ���� ���������
	pNode temp2; //��������� �� ������
	Node = Head; //������������� ��������� �� ������ ������
	int i = 0; //���������� �������
	system("cls"); //������� �����
	if (Head != NULL) { //���� ������ �� ����
		printf("���������� ��������� �� ������������ ����������");
			pNode q, out, p, pr;	//��������� �� ������
			out = NULL;                    // �������� ������ ����
			while (Node != NULL)              // ���� �� ���� ������� ������
			{
				q = Node; Node = Node->Next;  // ��������� ���������
				// ����� ����� ���������
				for (p = out, pr = NULL; p != NULL && strcmp(q->sorevnovanija.facultet, p->sorevnovanija.facultet) > 0; pr = p, p = p->Next); //���� ������ ������ �������
				if (pr == NULL)             // ��������� ����� ������
				{
					q->Next = out;  //�������������� ������
					out = q; //��������������� ������
				}
				else                      // ����� ����� �����������
				{
					q->Next = p; //�������������� ������
					pr->Next = q;//�������������� ������
				}
			}
			Head = out; //��������� ������ ������ ������ ������
	}
}


void sortNodeNumber(pNode& Head) {
	/*���������� ������� ��� ��������� ��������, ��������� �� �������� ����� ���������.*/
	boolean changed = true;   //���� �������� �� ������������.

	pNode Node; //��������� �� ������
	Sorevnovanija temp; //��������� ���������� ���� ���������
	pNode temp2; //��������� �� ������
	Node = Head; //������������� ��������� �� ������ ������
	int i = 0; //���������� �������
	system("cls"); //������� �����
	if (Head != NULL) { //���� ������ �� ����
		printf("���������� �������� ����� (����������  �������)");
			while (Node != NULL && changed) { //���� �� ����� ������, �� ���� ������ ������������� ������ �� �������. 

				changed = false;
				temp2 = Node->Next; //��������� ��������� �������
				while (temp2 != NULL ) //���� ��������� ����������
				{
					if (Node->sorevnovanija.srBall > temp2->sorevnovanija.srBall)   //�������� ��, ���� ������ ������ ������� ����� 
					{
						temp = Node->sorevnovanija;
						Node->sorevnovanija = temp2->sorevnovanija;
						temp2->sorevnovanija = temp;
						changed = true; // ���� ������� ������������� ��� ��������� ����� 
					}
					temp2 = temp2->Next; //������� � ����������
				}
				Node = Node->Next; //������� � ����������
			}
	}
}


void menu()
{
	int q = 0; //���������� ����
	pNode  Head = NULL; //��������� �� ������ ������
	pNode NewNode = NULL; //��������� �� ����� �������
	while (true) //����������� ����
	{
		system("cls"); //�������� �����
		printf(">>>>>>>>>>>>MENU<<<<<<<<<<<\n");
		printf(" 1 - ����� ����\n");
		printf(" 2 - ������� ����\n");
		printf(" 3 - ��������� ����\n");
		printf(" 4 - �������� �������\n");
		printf(" 5 - �������� ������\n");
		printf(" 6 - �������������� ������\n");
		printf(" 7 - ���������� �� ���������� (���������� ���������)\n");
		printf(" 8 - ���������� �� �������� ����� (���������� �������)\n");
		printf(" 9 - ����� ���� ������\n");
		printf("10 - �����\n");
		printf("������� ����� ����:\n");
		scanf("%d", &q); //������� �����  ����
		switch (q) //� ����������� �� ������ ��������� ��������
		{
		case 1:
			system("cls"); //�������� �����
			newFile(); //������� ������� �������� ������ �����
			break;
		case 2:
			system("cls"); //�������� �����
			Head = openFile(); //������� ������� �������� �����
			break;
		case 3:
			system("cls"); //�������� �����
			saveFile(Head); //������� ������� ���������� � ����
			break;
		case 4:
			system("cls"); //�������� �����
			Head = Add(Head); //������� ������� ����������
			break;
		case 5:
			system("cls"); //�������� �����
			deleteNode(Head); //������� ������� ��������
			break;
		case 6:
			system("cls"); //�������� �����
			EditNode(Head);//������� ������� ��������������
			system("pause");//�������� ������
			break;
		case 7:
			system("cls"); //�������� �����
			sortStringFacult(Head); //������� ������� ����������
			vivod(Head);//������� ������� ������
			system("pause");//�������� ������
			break;
		case 8:
			system("cls"); //�������� �����
			sortNodeNumber(Head); //������� ������� ����������
			vivod(Head);//������� ������� ������
			system("pause");//�������� ������
			break;
		case 9: 
			system("cls"); //�������� �����
			vivod(Head);//������� ������� ������
			system("pause"); //�������� ������
			break;
		case 10:
			system("cls"); //�������� �����
			exit(0); //�����
		default: printf("������� �������"); //������� ������
		}
	}
}