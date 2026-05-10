class Node:
    def __init__(self, info):
        self.info = info
        self.next = None

# W Pythonie najlepiej zamknąć tę logikę w funkcji. 
# Przekazujemy do niej obecny początek listy (head) oraz wartość do dodania (a).
def insert_sorted(head, a):
    
    # 1. Lista jest pusta (if list == NULL)
    if head is None:
        new_node = Node(a)
        return new_node  # Zwracamy nowy element, który staje się początkiem listy
        
    # 2. Wstawianie na samym początku listy (if list->info > a)
    if head.info > a:
        new_node = Node(a)
        new_node.next = head
        return new_node  # Zwracamy nowy początek listy
        
    # 3. Wstawianie w środku lub na końcu listy (sekcja else)
    tmp = head
    
    # Szukamy miejsca, dopóki nie dojdziemy do końca (tmp.next is not None) 
    # i dopóki kolejny element jest mniejszy niż nasze 'a'
    while tmp.next is not None and tmp.next.info < a:
        tmp = tmp.next
        
    # Tworzymy nowy węzeł (tmp2) i wpinamy go w listę
    tmp2 = Node(a)
    tmp2.next = tmp.next  # Nowy element wskazuje na to, na co wskazywał tmp
    tmp.next = tmp2       # Element tmp wskazuje teraz na nasz nowy element
    
    return head  # Zwracamy oryginalny początek listy, bo się nie zmienił

# -------------------------------------------------- struktura drzewa
class TreeNode:
    def __init__(self, info):
        self.info = info
        self.left = None
        self.right = None

# -------------------------------------------------- budowa drzewa
def insert(root, x):
    # Jeśli węzeł jest pusty (odpowiednik if(!root) i malloc w C)
    if root is None:
        return TreeNode(x)
        
    # Jeśli wartość jest mniejsza, idziemy w lewo
    if root.info > x:
        root.left = insert(root.left, x)
    # Jeśli wartość jest większa, idziemy w prawo
    elif root.info < x:
        root.right = insert(root.right, x)
        
    # Zwracamy korzeń (zaktualizowany węzeł)
    return root

# ------------------------------- szukanie elementu (dokończone)
def search(root, x):
    ptr = root
    while ptr is not None:
        if x > ptr.info:
            ptr = ptr.right
        elif x < ptr.info:
            ptr = ptr.left
        else:
            return ptr  # Znaleziono element (x == ptr.info)
            
    return None  # Jeśli pętla się skończy i nic nie znajdzie, zwraca None

# ------------------------------- 3 porządki przechodzenia drzew
def inorder(root):
    if root is not None:
        inorder(root.left)
        print(root.info, end=" ")
        inorder(root.right)

def postorder(root):
    if root is not None:
        postorder(root.left)
        postorder(root.right)
        print(root.info, end=" ")

def preorder(root):
    if root is not None:
        print(root.info, end=" ")
        preorder(root.left)
        preorder(root.right)
