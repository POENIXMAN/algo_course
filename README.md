# ALGO_COURSE: Решения алгоритмических задач

Этот репозиторий содержит решения различных алгоритмических задач, которые являются частью модуля алгоритмов. Решения реализованы на Python и организованы в виде отдельных Jupyter ноутбуков и скриптов Python для удобства чтения и тестирования. Каждая задача снабжена подробными объяснениями и кодом, с анализом сложности, представленным в комментариях в начале каждого решения.

## Содержание

- `problem1.ipynb` - Реверсирование односвязного списка
- `problem2.ipynb` - Формула релевантности
- `problem3.ipynb` - Инвертирование бинарного дерева поиска
- `problem4.ipynb` - Балансировка красно-черного дерева
- `problem5.ipynb` - Реализация красно-черного дерева для хранения пар "ключ-значение"
- `problem6.ipynb` - Определение дня с наибольшим количеством посетителей в отеле
- `problem7.ipynb` - Алгоритм Беллмана-Форда для произвольных графов
- `problem8.ipynb` - Венгерский алгоритм для задач комбинаторной оптимизации

## Обзор файлов

- `graph.py`: Содержит вспомогательные функции и классы для работы с графами, которые используются в некоторых решениях.
- `red_black_tree.py`: Реализация красно-черного дерева на Python, используемая в некоторых решениях задач.
- `README.md`: Этот файл с документацией, который предоставляет обзор содержимого репозитория и инструкции по использованию.

## Инструкции

1. Каждая задача представлена в отдельном Jupyter ноутбуке, что делает код и объяснения легко доступными для понимания.
2. Чтобы запустить ноутбуки, убедитесь, что у вас установлены Python и Jupyter. Используйте следующие команды:
    ```sh
    pip install jupyter
    jupyter notebook
    ```
3. После запуска Jupyter, перейдите к нужному ноутбуку с задачей и изучите решения.
4. Python-скрипты (`graph.py` и `red_black_tree.py`) предоставляют повторно используемые структуры данных и вспомогательные функции для некоторых задач.


## Описание задач

1. **Реверсирование односвязного списка** (`problem1.ipynb`): Этот ноутбук содержит решение для реверсирования односвязного списка с подробным объяснением времени выполнения и пространственной сложности.
2. **Формула релевантности** (`problem2.ipynb`):Задача включает использование упрощенной версии формулы релевантности для линейной комбинации признаков. Каждому объекту сопоставляется значение релевантности, рассчитываемое на основе весов признаков, причем значения признаков могут изменяться в процессе выполнения запросов. Решение содержит алгоритм для ранжирования объектов по релевантности и обновления их признаков в соответствии с запросами, а также оптимизации производительности при выполнении операций.

3. **Инвертирование бинарного дерева поиска** (`problem3.ipynb`): В этом ноутбуке представлено решение по инвертированию бинарного дерева поиска, чтобы узлы справа от материнского узла были больше, а слева — меньше.
4. **Балансировка красно-черного дерева** (`problem4.ipynb`): Этот ноутбук содержит алгоритм балансировки красно-черного дерева для обеспечения равномерности высоты дерева и эффективности операций.
5. **Реализация структуры данных на базе красно-черного дерева** (`problem5.ipynb`): Решение включает создание структуры данных для хранения пар "ключ-значение" на основе красно-черного дерева.
6. **Определение дня с наибольшим количеством посетителей в отеле** (`problem6.ipynb`): Этот ноутбук содержит алгоритм для определения дня, в который в отеле одновременно находилось наибольшее количество посетителей.
7. **Алгоритм Беллмана-Форда для произвольных графов** (`problem7.ipynb`): Решение включает реализацию алгоритма Беллмана-Форда для нахождения кратчайших путей в графе с возможными отрицательными весами рёбер.
8. **Венгерский алгоритм для задач комбинаторной оптимизации** (`problem8.ipynb`): Этот ноутбук содержит реализацию венгерского алгоритма для решения задач комбинаторной оптимизации, таких как задача о назначениях.


