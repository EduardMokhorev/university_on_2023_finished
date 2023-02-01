const consoleElement = document.querySelector('#console');
const execute = document.querySelector('.execute');
const taskOptions = document.querySelectorAll('.task-option');
const header = document.querySelector('.header');
const input = document.querySelector('.input');

let task = 'first'


header.addEventListener('click', controller);
execute.addEventListener('click', executeEvent);


function controller(event) {
  const target = event.target.dataset.task;
   
  if (target) {
    taskOptions.forEach(element => {
      if (element.dataset.task === target) {
        element.classList.add('current');
      }
      else {
        element.classList.remove('current');
      }
    })
    task = target;
  }
}


function getArrayValue(isString = false) {
  if (isString) {
    return input.value
    .split(' ')
    .filter(element => element !== '');
  }
  else {
    return input.value
    .replaceAll(',',' ')
    .split(' ')
    .filter(element => element !== '');
  }
}


// определяем какое задание выбрали.
function executeEvent() {
  consoleElement.innerHTML = " ";
  switch(task) {
    case 'first' :
      firstTask();
      break;
      
    case 'second' :
      secondTask();
      break;

    case 'third' :
      thirdTask();
      break;

    case 'fourth' :
      fourthTask();
      break;

    case 'fifth' :
      fifthTask();
      break;  
  }

  input.value = '';
}



//задание 1
// подсчитать кол-во положительных эллементов до максимального.
function firstTask() {
  const arr = getArrayValue();
  const max_element_in_array = Math.max.apply(null,arr)
  let count_elements_in_arrey_before_max = 0

  // проверка на число и на длинну массива.
  if (isNaN(max_element_in_array) || arr.length < 1){
    consoleElement.innerHTML = `Пожалуйста сформируйте массив парильно, можно использовать только числа.</br>` + consoleElement.innerHTML;
    return 0
  }
  consoleElement.innerHTML = `Исходный массив =  ${arr}.</br> Максимальный эллемент = ${max_element_in_array}.` + consoleElement.innerHTML;

  // Если максимальный эллемент равен или меньше нулю, считать кол-во положительных эллементов бесполезно.
  if (max_element_in_array <= 0){
    consoleElement.innerHTML = `Кол-во положительных эллементов до максимального =  ${0}</br>` + consoleElement.innerHTML;
    return 0
  }

  // проходим по массиву, если число положительное добавляем кол-во в счетчик, до тех пор пока не дойдем до максимального числа.
  let i = 0
  while (arr[i] != max_element_in_array) {
    if (arr[i] > 0) {
      count_elements_in_arrey_before_max += +1
    }
    i++;
  }
  consoleElement.innerHTML = `Кол-во положительных эллементов до максимального =  ${count_elements_in_arrey_before_max}</br>` + consoleElement.innerHTML;
}



//Дан целочисленный вектор A(2n). Если в векторе сумма S1=a1+ a2+...+an равна
// сумме S2=an+1+ an+2+...+ a2n, то поменять местами первый и последний элементы ветора.
// На печать выдавать исходный вектор, суммы S1, S2, преобразованный вектор. 
function secondTask() {
  const arr = getArrayValue();
  if (arr.length % 2 != 0){
    consoleElement.innerHTML = `Кол-во эллементов массива не может быть не четным, все эллементы массива должны быть целочисленными </br>` + consoleElement.innerHTML;
    return 0
  }
  let sum_s1 = 0; // сумма S1
  let sum_s2 = 0; // сумма S2

  // считаем сумму s1
  for (let i = 0; i < arr.length / 2 ; i++) {
    sum_s1 = +arr[i] + sum_s1;
  }

  // считаем сумму s2
  for (let i = arr.length / 2; i < arr.length; i++) {
    sum_s2 = +arr[i] + sum_s2;
  }
  if (isNaN(sum_s1) || isNaN(sum_s2)){
    consoleElement.innerHTML = `все эллементы массива должны быть целочисленными </br>` + consoleElement.innerHTML;
    return 0
  }
  // если s1 == s2 меняем первый и последний эллемент.
  if (sum_s1 == sum_s2){
    consoleElement.innerHTML = `Начальный массив: [${arr}] </br>` + consoleElement.innerHTML;

    temp = arr[0];
    arr[0] = arr[arr.length-1];
    arr[arr.length-1] = temp

    consoleElement.innerHTML = `Конечный массив массив: [${arr}]</br>` + consoleElement.innerHTML;
  }
  // иначе оставляем массив без изменения.
  else {
    consoleElement.innerHTML = `Начальный массив: [${arr}], Т.к. S1 != S2 массив не изменился</br>` + consoleElement.innerHTML;
  }
}



// Метод просеивания
function thirdTask() {
  const arr = getArrayValue();
  consoleElement.innerHTML = `Начальный массив: [${arr}] </br>` + consoleElement.innerHTML;
  for(let j = 0;j < arr.length -1;j++){
    for (let q = j+1; q < arr.length;q++){
      if(+arr[j] > +arr[q]){
        tmp = arr[j];
        arr[j] = arr[q];
        arr[q] = tmp;
      }
    }
  }

  consoleElement.innerHTML = `Конечный массив массив: [${arr}]</br>` + consoleElement.innerHTML;
} 



//                            12 вариант
// Напишите функцию, которая возвращает вторую цифру заданного целого числа
// в виде английского слова. Примеры: 521 > "two", 1422 > "four", 19302 >"nine"
function fourthTask() {
  // Создали массив для удобства, индекс массива содержит имя на английском.
  let numbers = ['zero','one','two','three','four','five','six','seven','eight','nine'];
  //input_value = input.value.replace(/ /g,'')         // В переменную положили значение input'a и убрали все пробелы
  input_value = input.value
  input_value = input_value.trim()
  check_int = Number(input_value)
  // Если это не число выводим сообщение и заканчиваем работу функции
  if (isNaN(check_int) || input_value.length < 2){
    consoleElement.innerHTML = `${'Строка должна содержать только одно число, которое состоит из 2х или больше значений'}</br>` + consoleElement.innerHTML;
    return 0
  }
  // Иначе Slise и вывоводим эллемент массива nubmers а его индекс укажем как input_value.slice
  consoleElement.innerHTML = `${numbers[input_value.slice(1,2)]}</br>` + consoleElement.innerHTML;
}



//                                                Вариант 12
//Создать новый текст, содержащий все слова исходного текста, которые оканчиваются на ту же букву, что и слово максимальной длины.
function fifthTask() {

  const arr = getArrayValue(true);
  let newArr = []
  console.log(arr)
  let maxWord = arr[0];
  let lastLetter = "";
  
  // Проходимся по массиву находим слово макс длинны.
  arr.forEach(word => {
    if (word.length > maxWord.length) {
      maxWord = word;
    }
  })
  lastLetter = maxWord.slice(-1) //последняя буква

  // Если последяя буква слова такая же как и в самом длинном слове в массиве то помещяем его в новый массив.
  arr.forEach(word => {
    if (word.slice(-1) == lastLetter){
       newArr.push(word)
    }
  })
  // вывод
  consoleElement.innerHTML = ` Самое длинное слово: ${maxWord} </br> Исходный массив = ${arr} </br> Результирующий массив = ${newArr.join(' ')} </br>` + consoleElement.innerHTML;
}