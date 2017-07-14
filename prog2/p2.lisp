;;; Program 2

;;; Checks if an atom is a top-level member of a set
(defun MEMSET (atm L)
    (COND ( (NULL L) NIL )
          ( (EQL atm (CAR L)) T )
          ( T  (MEMSET atm (CDR L)) )
    )
)

;;; Passes two lists, checks the top level,
;;; and returns the differences in the lists.
(defun SETDIFF (set1 set2)
    (COND ( (NULL set1) () )
          ( (NULL set2) set1)
          ( (MEMSET (car set1) set2)
                (SETDIFF (cdr set1) set2 )
          )
          ( T  (cons (car set1)
                     (setdiff (cdr set1) set2)
               )
          )
    )
)

;;; Passes a top level level lists and returns
;;; a list of unique atoms. (Order is insignificant)
(defun MAKESET (L)
    (COND ( (NULL L) NIL )
          ( (memset (car L)
                    (cons (cdr L)
                          (makeset (cdr L))
                    )
            )
                (makeset (cdr L))
          )
          ( T  (cons (car L)
                     (makeset (cdr L))
               )
          )
    )
)

;;; Passes a list containing any level of nesting and
;;; returns the list of atoms all in the same level.
(defun ATOMICLIST (L)
    (COND ( (NULL L) () )
          ( (ATOM (car L))
                (cons (car L)
                      (atomiclist (cdr L))
                )
          )
          ( T (append (atomiclist (car L))
                      (atomiclist (cdr L))
              )
          )
     )
)

;;; Passes a top level list and returns the number
;;; of elements in the list.
(defun CARDINALITY (L)
    (COND ( (NULL L) 0 )
          ( (NULL (car L)) (+ 0(cardinality (cdr L))) )
          ( T (+ 1(CARDINALITY (cdr L))) )
    )
)

;;; Passes a list containting any level of nesting and
;;; returns all unique non-nil atoms that occur anywhere in the list.
(defun countUniqNonNIL (L)
    (COND ( (NULL L) 0 )
          ( T (cardinality(makeset(atomiclist L))) )
    )
)
