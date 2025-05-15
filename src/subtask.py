from lab_7 import kmp_search
import os


def read_comments_from_file(filename):
    with open(filename, "r", encoding="utf-8") as f:
        return [line.strip() for line in f if line.strip()]


def write_comments_to_file(filename, comments, folder="../Classified_comments"):
    os.makedirs(folder, exist_ok=True)
    path = os.path.join(folder, filename)
    with open(path, "w", encoding="utf-8") as f:
        for comment in comments:
            f.write(comment + "\n")


def classify_comment(comment):
    c = comment.lower()

    positive_words = [
        "сподобалось",
        "дуже сподобалось",
        "класно",
        "чудово",
        "чудовий",
        "чудова",
        "чудове",
        "гарно",
        "гарна",
        "гарний",
        "супер",
        "молодець",
        "дякую",
        "велике дякую",
        "зрозумів",
        "зрозуміло",
        "допомогло",
        "легко",
        "корисно",
        "корисний",
        "корисна",
        "цікаво",
        "дуже цікаво",
        "приємно дивитися",
        "професійно",
        "найкраще",
        "найкращий",
        "найкраща",
        "рекомендую",
        "вперше зрозумів",
        "все ясно",
        "все чітко",
        "все логічно",
        "без зауважень",
        "крутий контент",
        "браво",
        "приємна подача",
        "логічно викладено",
        "структуровано",
        "продовжуйте",
        "молодці",
        "розумно",
        "актуально",
        "вчасно",
        "доступно",
        "кращі",
        "сподобалось",
        "сподобалась",
        "клас",
        "дякую",
        "найкращі",
        "складно але",
    ]

    criticism_words = [
        "даремно",
        "не сподобалось",
        "не зрозумів",
        "незрозуміло",
        "погано",
        "поганий",
        "покращ",
        "виправ",
        "слабко",
        "слабка",
        "слабо",
        "нудно",
        "недостатньо",
        "можна краще",
        "мало суті",
        "мало прикладів",
        "мало",
        "забагато",
        "заплутано",
        "занадто довге",
        "занадто швидко",
        "надто довго",
        "надто довге",
        "надто швидко",
        "хотілося б",
        "не розумію",
        "потрібно більше",
        "потрібно менше",
        "потрібно пояснення",
        "немає пояснень",
        "потрібні пояснення",
        "треба більше деталей",
        "треба більше прикладів",
        "старайся",
        "робіть краще",
        "будь ласка, поясніть",
        "швидко пояснюєте",
        "голос різкий",
        "неактуально",
        "не все зрозуміло",
        "двозначно",
        "без структури",
        "розпливчасто",
        "немає логіки",
        "відволікає",
        "непрофесійно",
        "повторюється",
        "сухо подано",
        "важко слідкувати",
        "можна",
        "треба",
        "потрібно",
        "зробіть",
        "було б",
        "не вистачає",
        "не",
        "варто",
        "складно",
        "бракує",
    ]

    hate_words = [
        "дурень",
        "дурна подача",
        "жахливе",
        "спам",
        "відстій",
        "нікчема",
        "злив часу",
        "лайно",
        "тупо",
        "некомпетентно",
        "ганьба",
        "школяр би краще зробив",
        "повна маячня",
        "хто це знімав",
        "знущання",
        "несмак",
        "автор ніякий",
        "гірше не бачив",
        "видаліть це",
        "ніколи більше",
        "нема слів",
        "треш",
        "ганьба контенту",
    ]

    positive = sum(kmp_search(w, c) for w in positive_words)
    criticism = sum(kmp_search(w, c) for w in criticism_words)
    hate = sum(kmp_search(w, c) for w in hate_words)

    counts = {"Hate": hate, "Criticism": criticism, "Positive": positive}

    max_category = max(counts, key=counts.get)

    return max_category


if __name__ == "__main__":
    input_file = "../comments.txt"

    comments = read_comments_from_file(input_file)

    groups = {"Positive": [], "Criticism": [], "Hate": []}

    for comment in comments:
        category = classify_comment(comment)
        groups[category].append(comment)

    write_comments_to_file("positive.txt", groups["Positive"])
    write_comments_to_file("criticism.txt", groups["Criticism"])
    write_comments_to_file("hate.txt", groups["Hate"])
