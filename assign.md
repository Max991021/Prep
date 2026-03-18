Learning Outcomes assessed

    Data Structures
    Data Manipulation
    Recursion
    String Formatting

Assessment Structure

The following Assessment has two sections:

    Coding Assessment (Questions are below)
    Long Questions (Questions are below) - answers.txt

You can answer them in any order.
Your Goal

Read the instructions below for each coding question, then complete each function in data_structures.py while ensuring that:

    The code is valid Python
    Each function behaves according to the instructions
    All unit tests pass successfully

Read the instructions below for each long format question, then add your answer under each relevant comment in answers.txt while ensuring that:

    You DO NOT remove the comments
    Read each question carefully before answering the question

How to run your tests

To run all your tests

python3 -m pytest tests/test_data_structures.py -v

To run your tests individually

python3 -m pytest tests/test_data_structures.py::test_pair_coordinates_logic -v

or for more information within the stacktrace use

python3 -m pytest tests/test_data_structures.py::test_pair_coordinates_logic -vv

Scoring & Weighting
Component	Weight
Coding Section (unit tests)	50%
Long-format Question (answers.txt)	50%
Fundamentals Coding Assessment

This assessment consists of seven Python functions. Each function has a partially written implementation. Your task is to fix the bugs, complete the missing logic, and ensure all tests pass.
Project Structure

fun-004-data-structures/
├── data_structures.py              # <-- This is where you write your solutions
├── answers.txt                     # <-- This is where you write your answers to the long questions
├── tests/
│   └── test_data_structures.py     # <-- These are the tests you must make pass
└── README.md                       # <-- Assessment instructions (this file) 

### Question 1 - `pair_coordinates(x_vals, y_vals) `

The Cape Town Cycle Tour organisers in the City Bowl have two separate data streams coming from their GPS tracking system — one list of x positions and one list of y positions for each checkpoint along the route. To plot the route on their mapping software, the tech team needs these two streams merged back into a single list of coordinate pairs.

Apply your logic to the pair_coordinates() function. You will receive two lists of equal length and must return a list of tuples, where each tuple pairs the corresponding x and y values.

    Input:

x_vals = [12, 15, 18]
y_vals = [45, 48, 51]

    Output:

[(12, 45), (15, 48), (18, 51)]

### Question 2 - `count_occurrences(items)`

A Johannesburg-based social media startup is analysing trending hashtags posted during the FIFA World Cup qualifier matches at FNB Stadium. Their system collects thousands of raw hashtag strings throughout the day, and the analytics team needs to know how many times each unique hashtag appeared so they can surface the most popular ones on the trending page.

Apply your logic to the count_occurrences() function. You will receive a list of strings and must return a dictionary where each unique string is a key and its value is the number of times it appeared in the list.

    Input:

["Bafana", "Soccer", "Bafana", "Goals", "Soccer", "Bafana"]

    Output:

{"Bafana": 3, "Soccer": 2, "Goals": 1}

### Question 3 - `find_common_skills(applicants)`

A tech recruitment agency in the Sandton CBD is hosting a career fair for top South African engineering graduates. Each applicant has submitted a list of their skills. The hiring managers from various companies want to know which skills every single applicant has in common, so they can design a shared baseline technical test for all candidates.

Apply your logic to the find_common_skills() function. You will receive a dictionary where each key is an applicant's name and each value is a list of their skills. Return a set of skills that appear in every applicant's list.

    Input:

{
    "Lerato": ["Python", "SQL", "Git", "Docker"],
    "Thabo":  ["Python", "SQL", "Java", "Git"],
    "Nandi":  ["Python", "SQL", "Git", "React"]
}

    Output:

{"Python", "SQL", "Git"}

### Question 4 - `flatten_schedule(schedule)`

A high school in Soweto has just digitised their timetable system. The data was exported from an old spreadsheet in a nested format — a list of days, where each day contains a list of subjects. The new school management app needs the schedule as a single flat list of all subjects in order, so it can display them in a simple timeline view.

Apply your logic to the flatten_schedule() function. You will receive a list of lists and must return a single flat list containing all elements in order.

    Input:

[["Maths", "English"], ["Science", "History"], ["Art", "PE", "Coding"]]

    Output:

["Maths", "English", "Science", "History", "Art", "PE", "Coding"]

### Question 5 - `sliding_window_sum(numbers, window_size)`

Eskom's load management engineers in Megawatt Park, Sunninghill, are monitoring electricity consumption data collected every hour from a township substation. To smooth out spikes in the data, they use a sliding window technique — at each position, they calculate the total consumption across a fixed number of consecutive hours. This helps them identify sustained high-usage periods rather than single outlier readings.

Apply your logic to the sliding_window_sum() function. Given a list of numbers and a window size k, return a new list where each element is the sum of k consecutive elements starting at that position. The last window starts at index len(numbers) - k.

    Input:

numbers = [2, 4, 6, 8, 10]
window_size = 3

    Output:

[12, 18, 24]

Constraint: The output list will always have len(numbers) - window_size + 1 elements.
### Question 6 - `group_by_province(cities)`

Statistics South Africa (StatsSA) in Pretoria is preparing a national infrastructure report. Their raw dataset is a flat list of city records, each containing a city name and its province. The report template requires the data to be reorganised by province, listing all cities under their respective provincial heading so analysts can quickly compare urban development across regions.

Apply your logic to the group_by_province() function. You will receive a list of dictionaries, each with a "city" and a "province" key. Return a dictionary where each province is a key and its value is a list of all city names in that province.

    Input:

[
    {"city": "Durban",           "province": "KwaZulu-Natal"},
    {"city": "Pietermaritzburg", "province": "KwaZulu-Natal"},
    {"city": "Bloemfontein",    "province": "Free State"},
    {"city": "Welkom",          "province": "Free State"},
    {"city": "Polokwane",       "province": "Limpopo"}
]

    Output:

{
    "KwaZulu-Natal": ["Durban", "Pietermaritzburg"],
    "Free State":    ["Bloemfontein", "Welkom"],
    "Limpopo":       ["Polokwane"]
}

Long-Format Questions

Please answer these in the answers.txt file (DO NOT REMOVE THE COMMENTS AND DO NOT CHANGE THE FORMAT)
Comprehension Question 1 — Lists and Tuples

A fellow student at WeThinkCode_ is arguing that lists and tuples are basically the same thing and that there is no real reason to ever use a tuple. You disagree.
Explain to them what the difference is between a list and a tuple in Python, why that difference actually matters, and describe a situation where reaching for a tuple instead of a list is the right call.
Comprehension Question 2 — Sets and Duplicates

You are working on a data pipeline at a Cape Town e-commerce company. Your team has been collecting customer email addresses from multiple sources and suspects there are thousands of duplicates in the data. A teammate suggests looping through the entire list and manually checking for duplicates. You know there is a better way.

Explain what a set is in Python, how it behaves differently from a list, and why it would be a better tool for solving this specific problem. Also explain what you give up when you use a set instead of a list.
Comprehension Question 3 — Choosing the Right Data Structure

A small clinic in Pretoria has asked your team to build a system to manage their patient waiting room. Patients arrive throughout the day and must be seen strictly in the order they arrived — the first patient to check in must be the first patient called in, no exceptions. The system also needs to be able to add new patients as they arrive and remove a patient once they have been called in.

Without being told which data structure to use, explain which Python data structure you would choose to model this waiting room, why it is the most appropriate choice, and why the other basic Python data structures would not be as suitable for this problem.