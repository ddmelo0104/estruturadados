from tree import Tree


def normalize(word: str) -> str:
    """Padroniza a palavra (sem espaços nas pontas e em minúsculas) para que
    a busca e a ordenação sejam sempre consistentes."""
    return word.strip().lower()


def load_examples(tree: Tree) -> None:
    """Carrega um glossário de exemplo (termos de programação)."""
    examples = {
        "algoritmo": "Sequência finita de passos para resolver um problema.",
        "arvore": "Estrutura de dados hierárquica formada por nós e ramos.",
        "no": "Cada elemento de uma árvore; guarda um dado e liga a outros nós.",
        "recursao": "Técnica em que uma função chama a si mesma.",
        "variavel": "Espaço na memória usado para guardar um valor.",
        "funcao": "Bloco de código reutilizável que executa uma tarefa.",
        "loop": "Estrutura que repete um bloco de código várias vezes.",
        "lista": "Coleção ordenada de elementos.",
        "pilha": "Estrutura LIFO: o último a entrar é o primeiro a sair.",
        "fila": "Estrutura FIFO: o primeiro a entrar é o primeiro a sair.",
    }
    for word, definition in examples.items():
        tree.add(word, definition)
    print(f"\n✓ {len(examples)} palavras de exemplo foram carregadas!")


# ---------------------------------------------------------------------------
# Ações do menu
# ---------------------------------------------------------------------------
def add_word(tree: Tree) -> None:
    word = normalize(input("Palavra: "))
    if not word:
        print("\n✗ Palavra inválida.")
        return
    definition = input("Definição: ").strip()
    if not definition:
        print("\n✗ A definição não pode ficar vazia.")
        return

    exists = tree.search(word) is not None
    tree.add(word, definition)
    if exists:
        print(f"\n✓ Definição de '{word}' atualizada.")
    else:
        print(f"\n✓ '{word}' adicionada ao dicionário.")


def search_word(tree: Tree) -> None:
    word = normalize(input("Palavra a buscar: "))
    node = tree.search(word)
    if node:
        print(f"\n {node.content.capitalize()}")
        print(f"   {node.definition}")
    else:
        print(f"\n✗ '{word}' não está no dicionário.")


def remove_word(tree: Tree) -> None:
    word = normalize(input("Palavra a remover: "))
    if tree.search(word) is None:
        print(f"\n✗ '{word}' não está no dicionário.")
        return
    tree.remove(word)
    print(f"\n✓ '{word}' removida do dicionário.")


def list_dictionary(tree: Tree) -> None:
    if tree.count() == 0:
        print("\n(dicionário vazio)")
        return
    print("\n===== DICIONÁRIO (ordem alfabética) =====")
    tree.list_entries()


def show_traversals(tree: Tree) -> None:
    if tree.count() == 0:
        print("\n(dicionário vazio)")
        return
    print("\nEm-ordem  (Esq -> Raiz -> Dir)  — sai em ordem alfabética:")
    tree.print_in_order()
    print("\nPré-ordem (Raiz -> Esq -> Dir):")
    tree.print_pre_order()
    print("\nPós-ordem (Esq -> Dir -> Raiz):")
    tree.print_post_order()


def show_statistics(tree: Tree) -> None:
    print(f"\n Palavras no dicionário: {tree.count()}")
    print(f"   Altura da árvore:       {tree.height()}")


# ---------------------------------------------------------------------------
# Loop principal do menu
# ---------------------------------------------------------------------------
def menu() -> None:
    tree = Tree()

    print("=" * 52)
    print("     DICIONÁRIO COM ÁRVORE BINÁRIA DE BUSCA")
    print("=" * 52)

    while True:
        print("\n----------------- MENU -----------------")
        print("1 - Adicionar / atualizar palavra")
        print("2 - Buscar palavra")
        print("3 - Remover palavra")
        print("4 - Listar dicionário (ordem alfabética)")
        print("5 - Demonstrar travessias (pré / em / pós-ordem)")
        print("6 - Estatísticas (nº de palavras e altura)")
        print("7 - Carregar palavras de exemplo")
        print("0 - Sair")

        option = input("\nEscolha uma opção: ").strip()

        if option == "1":
            add_word(tree)
        elif option == "2":
            search_word(tree)
        elif option == "3":
            remove_word(tree)
        elif option == "4":
            list_dictionary(tree)
        elif option == "5":
            show_traversals(tree)
        elif option == "6":
            show_statistics(tree)
        elif option == "7":
            load_examples(tree)
        elif option == "0":
            print("\nAté logo!")
            break
        else:
            print("\n✗ Opção inválida. Tente novamente.")


if __name__ == "__main__":
    menu()
