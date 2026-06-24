class Node:
    def __init__(self, content, definition):
        self.left: "Node" = None          # filho à esquerda (palavras "menores")
        self.right: "Node" = None         # filho à direita  (palavras "maiores")
        self.content: str = content       # a palavra -> usada para ordenar a árvore
        self.definition: str = definition  # o significado da palavra


class Tree:
    def __init__(self):
        self.root: "Node" = None

    # ======================================================================
    # INSERÇÃO  
    # ======================================================================
    def add(self, content, definition, root=None):
        # árvore vazia -> a palavra vira a raiz
        if self.root is None:
            self.root = Node(content, definition)
            return

        if root is None:
            root = self.root

        # a palavra já existe -> apenas atualiza a definição (sem duplicar)
        if content == root.content:
            root.definition = definition
            return

        # maior que o nó atual -> vai para a DIREITA
        if content > root.content:
            if root.right is None:
                root.right = Node(content, definition)
            else:
                self.add(content, definition, root.right)
        # menor que o nó atual -> vai para a ESQUERDA
        else:
            if root.left is None:
                root.left = Node(content, definition)
            else:
                self.add(content, definition, root.left)

    # ======================================================================
    # BUSCA  ->  retorna o nó da palavra (ou None se não existir)
    # ======================================================================
    def search(self, content):
        return self._search(self.root, content)

    def _search(self, root, content):
        if root is None:                 # chegou no fim sem achar
            return None
        if content == root.content:      # achou!
            return root
        if content < root.content:       # procura na subárvore esquerda
            return self._search(root.left, content)
        else:                            # procura na subárvore direita
            return self._search(root.right, content)

    # ======================================================================
    # REMOÇÃO 
    # ======================================================================
    def remove(self, content):
        """Remove uma palavra da árvore."""
        self.root = self._remove(self.root, content)

    def _remove(self, root, content):
        # palavra não encontrada -> nada muda
        if root is None:
            return None

        # ainda não chegou no nó: continua descendo
        if content < root.content:
            root.left = self._remove(root.left, content)
            return root
        if content > root.content:
            root.right = self._remove(root.right, content)
            return root

        # --- aqui content == root.content: este é o nó a remover ---

        # CASO 1 e 2: nó sem filho à esquerda (folha OU só com filho direito)
        # -> o lugar dele é ocupado pelo filho da direita (que pode ser None)
        if root.left is None:
            return root.right

        # CASO 2: nó só com filho à esquerda
        # -> o lugar dele é ocupado pelo filho da esquerda
        if root.right is None:
            return root.left

        # CASO 3: nó com DOIS filhos
        # -> substitui pelo "sucessor in-order": a menor palavra da
        #    subárvore direita (o nó mais à esquerda dela).
        successor = self._min_node(root.right)
        root.content = successor.content
        root.definition = successor.definition
        # remove o sucessor (que agora está duplicado) da subárvore direita
        root.right = self._remove(root.right, successor.content)
        return root

    def _min_node(self, root):
        """Retorna o nó com a menor palavra (o mais à esquerda)."""
        current = root
        while current.left is not None:
            current = current.left
        return current

    # ======================================================================
    # TRAVESSIAS 
    # ======================================================================
    def print_in_order(self, root=None):
        """Em-ordem: Esquerda -> Raiz -> Direita (sai em ordem alfabética)."""
        if root is None:
            root = self.root
        if root:
            if root.left:
                self.print_in_order(root.left)
            print(root.content)
            if root.right:
                self.print_in_order(root.right)

    def print_pre_order(self, root=None):
        """Pré-ordem: Raiz -> Esquerda -> Direita."""
        if root is None:
            root = self.root
        if root:
            print(root.content)
            if root.left:
                self.print_pre_order(root.left)
            if root.right:
                self.print_pre_order(root.right)

    def print_post_order(self, root=None):
        """Pós-ordem: Esquerda -> Direita -> Raiz."""
        if root is None:
            root = self.root
        if root:
            if root.left:
                self.print_post_order(root.left)
            if root.right:
                self.print_post_order(root.right)
            print(root.content)

    # ======================================================================
    # LISTAGEM DO DICIONÁRIO  (em-ordem, mostrando palavra + definição)
    # ======================================================================
    def list_entries(self, root=None):
        if root is None:
            root = self.root
        if root:
            if root.left:
                self.list_entries(root.left)
            print(f"  • {root.content.capitalize()} — {root.definition}")
            if root.right:
                self.list_entries(root.right)

    # ======================================================================
    # ESTATÍSTICAS
    # ======================================================================
    def count(self):
        """Conta quantas palavras (nós) existem na árvore."""
        return self._count(self.root)

    def _count(self, root):
        if root is None:
            return 0
        return 1 + self._count(root.left) + self._count(root.right)

    def height(self):
        """Altura da árvore (caminho mais longo da raiz até uma folha)."""
        return self._height(self.root)

    def _height(self, root):
        if root is None:
            return 0
        return 1 + max(self._height(root.left), self._height(root.right))
