#include <locale.h> //��� �������� �����
#include <stdio.h> //��� ������ printf

int pos(char* str, const char* substr)
{
   char *temp = str; //�������� ������ �� ��������� ����������
   char* t;
   const char* s;
    for (; *str; ++str)   		//��������� ���� �� ���� �������� ������
	{
        for (t = str, s = substr; *t && *s && (*t == *s); ++t, ++s); //���� �� ������ ������, �� ������ ���������, ���� s � t �� ����� � �����, ����������� �������
      		if (*s == 0) //���� s �����������
      			{
            		break; //������� �� �����
            	}            	
   	}
   	int count=0; //�������� ����������
   int r = str-temp; //������� ������� ���������, ���� ������� ��������� ���, �� ����� ����� ����� ������	
   for (; *temp; ++temp)   		
	{
		count++; //������������ ���������� �������� � �������� ������
	}
   if (r==count) return -1; //���� �����, �� ���������� ��������, ��� ������ �� �����
   else return r; //����� ���������� ������� ���������
}

int main()
{
	setlocale(LC_ALL, "Rus");
	char str[255];
	char substr[255];
	printf("������� ���� ������: ");
	scanf("%s", str);
	printf("������� ���������: ");
	scanf("%s", substr);
	int k = pos(str, substr);
	if (k<0)
	printf("������� ���������: �� �������");
	else
	printf("������� ���������: %d", k+1);
}
