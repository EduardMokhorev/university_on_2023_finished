#include <locale.h> //дл€ русского €зыка
#include <stdio.h> //дл€ работы printf

int pos(char* str, const char* substr)
{
   char *temp = str; //копируем строку во временную переменную
   char* t;
   const char* s;
    for (; *str; ++str)   		//запускаем цикл по всем символам строки
	{
        for (t = str, s = substr; *t && *s && (*t == *s); ++t, ++s); //цикл от начала строки, от начала подстроки, пока s и t не пусты и равны, увеличиваем символы
      		if (*s == 0) //если s закончилась
      			{
            		break; //выходим из цикла
            	}            	
   	}
   	int count=0; //обнул€ем переменную
   int r = str-temp; //находим позицию вхождени€, если позиции вхождени€ нет, то будет равна длине строки	
   for (; *temp; ++temp)   		
	{
		count++; //подсчитываем количество символов в исходной строку
	}
   if (r==count) return -1; //если равны, то возвращаем значение, что ничего не нашли
   else return r; //иначе возвращаем позицию вхождени€
}

int main()
{
	setlocale(LC_ALL, "Rus");
	char str[255];
	char substr[255];
	printf("¬ведите вашу строку: ");
	scanf("%s", str);
	printf("¬ведите подстроку: ");
	scanf("%s", substr);
	int k = pos(str, substr);
	if (k<0)
	printf("ѕозици€ вхождени€: не найдено");
	else
	printf("ѕозици€ вхождени€: %d", k+1);
}
