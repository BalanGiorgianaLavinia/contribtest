    Functia "list_files" afiseaza toate fisierele .rst din calea data ca parametru.

    Functia "read_file" citeste din fisier metadatele pana intalneste linia cu '---', 
apoi restul liniilor din fisier sunt considerate continutul. 
    
    Functia "write_output" scrie in fisierul de output codul html cu variabilele inlocuite
din fisierele.rst procesate in functia de mai sus.
    Numele noului fisier este acelasi cu numele fisierului de intrare.

    Functia "generate_site" primeste calea folderului in care se afla resursele si 
citeste din fisier metadatele si continutul folosind functia de read_file.
    Se creeaza un template pe baza fisierelor html si se inlocuiesc variabilele cu 
cele din dictionar de unde au fost parsate (din fisierele .rst).
    Codul html prelucrat este scris in fisier folosind functia de write_output.