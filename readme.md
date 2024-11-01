
### Алгоритмы

1. **Базовые алгоритмы**:
	- **Сортировки**:
	    - Пузырьковая сортировка
	    - Сортировка выбором
	    - Сортировка вставками
	    - Быстрая сортировка (QuickSort)
	    - Сортировка слиянием (MergeSort)
	    - Пирамидальная сортировка (Heapsort)
	- **Поиск**:
	    - Бинарный поиск
	- **Алгоритмы работы с числами**:
	    - Нахождение НОД, НОК (алгоритм Евклида)
	    - Проверка числа на простоту (пробный делитель, решето Эратосфена)
	    - Разложение числа на простые множители
	    - Быстрое возведение в степень (алгоритм бинарного возведения в степень)

2. **Динамическое программирование**:
	- **Классические задачи**:
	    - Задача о рюкзаке (с одним или несколькими видами предметов)
	    - Задача о размене монет
	    - Задача о наибольшей общей подпоследовательности (LCS)
	    - Задача о наибольшей общей подстроке
	    - Задача о наибольшей возрастающей подпоследовательности (LIS)
	    - Задача о максимальной подматрице и подотрезке (алгоритм Кадане)
	    - Подсчёт количества путей в сетке
	    - Задача на разбиение числа

3. **Жадные алгоритмы**:
	- Алгоритм для задачи о размене монет
	- Алгоритмы для задач покрытия отрезков и множеств
	- Задачи на выбор максимального или минимального набора элементов

4. **Алгоритмы на графах**:
	- **Обходы графов**:
	    - Обход в глубину (DFS)
	    - Обход в ширину (BFS)
	- **Алгоритмы поиска кратчайшего пути**:
	    - Алгоритм Дейкстры (для графов без отрицательных рёбер)
	    - Алгоритм Беллмана-Форда (для графов с отрицательными рёбрами)
	    - Алгоритм Флойда-Уоршелла (поиск кратчайших путей между всеми парами вершин)
	- **Алгоритмы поиска минимального остовного дерева**:
	    - Алгоритм Прима
	    - Алгоритм Краскала
	- **Топологическая сортировка** для направленного ациклического графа (DAG)
	- **Алгоритмы на связность графа**:
	    - Поиск компонент связности (DFS, BFS)
	    - Поиск мостов и точек сочленения (алгоритм Тарьяна)
	    - Поиск сильно связных компонент (алгоритм Косарайю)

5. **Работа со строками**:
	- **Алгоритмы поиска подстрок**:
	    - Наивный алгоритм
	    - Алгоритм Кнута-Морриса-Пратта (КМП)
	    - Алгоритм Бойера-Мура
	- **Работа с префиксными и суффиксными массивами**:
	    - Префикс-функция для строки
	    - Суффиксный массив
	- **Алгоритм Z-функции** для поиска шаблонов в строках
	- **Работа с хешами** для строк (например, метод Рабина-Карпа)

6. **Геометрические алгоритмы**:
	- Проверка принадлежности точки многоугольнику
	- Нахождение расстояния между точками, точкой и отрезком
	- Алгоритмы на пересечение отрезков
	- Выпуклая оболочка (алгоритм Грэхема, алгоритм Джарвиса)
	- Площадь многоугольника

7. **Структуры данных**:
	- **Стек и очередь**
	- **Дек** (двусторонняя очередь)
	- **Куча** (Min-Heap, Max-Heap)
	- **Дерево поиска**:
	    - Бинарное дерево поиска
	    - Сбалансированные деревья (красно-чёрные деревья, AVL-деревья)
	- **Хеш-таблицы**
	- **Дерево отрезков** и **дерево Фенвика** (для выполнения быстрых операций над отрезками)
	- **Trie (префиксное дерево)** для работы со строками
	- **Суффиксное дерево** и **суффиксный массив**

8. **Комбинаторика и перебор**:
	- Перебор всех перестановок
	- Перебор всех сочетаний
	- Перебор всех подмножеств
	- Генерация подмножеств, перестановок и сочетаний с использованием рекурсии
	- Задачи с битовыми масками для подмножеств

9. **Алгоритмы работы с битами**:
	- Основные побитовые операции (AND, OR, XOR, NOT, сдвиги)
	- Подсчёт количества установленных битов
	- Проверка на чётность/нечётность числа с использованием битовых операций
	- Быстрое умножение и деление на степень двойки
	- Задачи на использование битовых масок для представления подмножеств

10. **Математические алгоритмы**:
	- Быстрое возведение в степень
	- Решение уравнений и систем уравнений (методом подстановки или с использованием алгоритма Гаусса)
	- Алгоритмы для работы с большими числами (например, вычисление факториалов или возведение в степень с модулем)

11. **Алгоритмы вероятностей и статистики**:
	- Подсчёт вероятностей и вычисление математического ожидания
	- Задачи на комбинирование вероятностей
	- Применение случайного выбора и генераторов случайных чисел

### Продвинутые алгоритмы

1. **Продвинутые алгоритмы на графах**:
	- **Алгоритм Флойда-Уоршелла с улучшением** — для поиска кратчайших путей с дополнительной оптимизацией.
	- **Алгоритм Джонсона** — для нахождения кратчайших путей между всеми парами вершин в графе с разреженными ребрами.
	- **Поиск мостов и точек сочленения** — для анализа связности графа (алгоритм Тарьяна с использованием чисел посещения и обратного пути).
	- **Алгоритмы поиска на максимальный поток**:
	    - Алгоритм Форда-Фалкерсона (базовый алгоритм для расчета максимального потока)
	    - Алгоритм Эдмондса-Карпа (улучшение Форда-Фалкерсона, работает за O(VE2)O(VE^2)O(VE2))
	    - Алгоритм Диница (более быстрый, эффективен для плотных графов, сложность O(V2E)O(V^2E)O(V2E))
	- **Задача о минимальном разрезе**:
	    - Алгоритм Гомори-Ху для нахождения всех минимальных разрезов между парами вершин.
	- **Двудольные графы**:
	    - Поиск максимального паросочетания (алгоритм Хопкрофта-Карпа для двудольных графов)
	    - Задача о назначениях (венгерский алгоритм для нахождения минимального взвешенного паросочетания)
	- **Алгоритм Тарьяна** для поиска сильно связных компонент в графах.

2. **Продвинутые алгоритмы на деревьях**:
	- **Декартово дерево** (Treap) — комбинирует свойства бинарного дерева поиска и кучи.
	- **Дерево отрезков с разреженными таблицами (Sparse Table)** — используется для вычисления значений на подотрезках массива с поддержкой ассоциативных операций.
	- **Дерево Фенвика (Fenwick Tree)** с расширениями для сложных операций.
	- **Декартово дерево по неявному ключу** — для операций над подотрезками и подмассивами.
	- **LCA (Lowest Common Ancestor)** — нахождение ближайшего общего предка двух узлов в дереве (алгоритмы с бинарным подъемом, методом таблиц или алгоритм Тарьяна).
	- **Центроидное разложение деревьев** — для оптимизации поиска на дереве и обработки запросов на подотрезках.

3. **Геометрические алгоритмы продвинутого уровня**:
	- **Алгоритм Грэма и алгоритм Джарвиса** для построения выпуклой оболочки в 3D.
	- **Алгоритм Фортуна для триангуляции Делоне** — построение триангуляции на плоскости.
	- **КД-дерево (k-d tree)** — для быстрого поиска ближайших соседей в многомерном пространстве.
	- **Алгоритмы вычисления расстояний в многомерных пространствах** — например, метод ближайших соседей.

4. **Алгоритмы обработки строк продвинутого уровня**:
	- **Суффиксный массив и суффиксное дерево**:
	    - Построение суффиксного массива за O(nlog⁡n)O(n \log n)O(nlogn) или O(n)O(n)O(n) времени (алгоритмы Касаи, алгоритм Манбера-Майерса).
	    - Суффиксный автомат для эффективной работы с подстроками.
	- **Алгоритм Aho-Corasick** — автомат для поиска нескольких шаблонов в строке, полезен для обработки большого количества запросов на подстроки.
	- **Алгоритмы хеширования строк**:
	    - Хеширование Рабина-Карпа с двойным хешем или полиномиальным хешем для улучшения устойчивости.
	- **Z-функция и префикс-функция** — используются для решения задач с шаблонами и подстроками.

5. **Комбинаторные алгоритмы продвинутого уровня**:
	- **Метод включения и исключения** — для сложных подсчётов сочетаний с условиями.
	- **Алгоритмы генерации перестановок и сочетаний** — такие как алгоритм Лексиографического и Алгоритм Йейтса (быстрая генерация).
	- **Генерация комбинаторных объектов (Gray code)** — позволяет генерировать перестановки и комбинации с минимальными изменениями.
	- **Алгоритмы для задачи о назначениях** — метод венгерского алгоритма для оптимизации назначений на максимизацию или минимизацию.

6. **Алгоритмы теории чисел продвинутого уровня**:
	- **Алгоритм решета Аткина и решето Эратосфена с сегментацией** — для поиска простых чисел на большом отрезке.
	- **Тесты простоты чисел**:
	    - Тест Ферма — простой и быстрый, но не точный.
	    - Тест Миллера-Рабина — вероятностный тест, популярный в олимпиадах.
	    - Тест Соловея-Штрассена — ещё один вероятностный тест на простоту.
	- **Факторизация чисел**:
	    - Алгоритм Полларда (rho-метод) для разложения числа на множители.
	    - Метод квадратичного решета и алгоритм Ленстры на эллиптических кривых.
	- **Алгоритмы для работы с модулярной арифметикой**:
	    - Быстрое возведение в степень по модулю (модульное экспоненцирование).
	    - Вычисление обратного элемента по модулю (расширенный алгоритм Евклида).
	    - Малой теорема Ферма и китайская теорема об остатках.

7. **Методы поиска с ограничениями (CSP)**:
	- **Методы ветвей и границ** — для задач на оптимизацию.
	- **Поиск с возвратом (backtracking)** — эффективные реализации с отсечениями.
	- **Задачи на динамическое программирование с отсечениями** (например, алгоритм A* для поиска кратчайшего пути).

8. **Алгоритмы для обработки массивов и подотрезков**:
	- **Mo’s Algorithm** — для эффективного ответа на запросы с подотрезками в статическом массиве.
	- **SQRT-декомпозиция** — для обработки запросов на отрезках, разбиение массива на блоки фиксированного размера.
	- **Имплицитные деревья отрезков** — для экономии памяти при больших массивах.

9. **Методы на вероятности и случайные процессы**:
	- **Monte Carlo и Las Vegas алгоритмы** — вероятностные алгоритмы для поиска решения, например, для факторизации и проверки на простоту.
	- **Методы случайных блужданий и Марковских цепей** — для моделирования и анализа процессов.

10. **Методы машинного обучения и анализа данных**:
	- **Методы кластеризации и классификации** — могут быть полезны для анализа данных в задачах, где требуются знания машинного обучения.
	- **Алгоритмы построения деревьев решений** — такие как CART или ID3, полезные для задач на поиск оптимальных стратегий.