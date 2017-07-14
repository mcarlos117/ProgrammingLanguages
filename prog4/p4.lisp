;;; Programming Assignment 4

;;; Given an expression, it will be converted into a
;;; well formed formula.
(defun WFF (L)
    (COND
        ;;; Check if atom (check if number or plain x)
        ( (atom L) L )
        ;;; Checks for cases without number after x
        ( (NULL (cddr L))
            (WFF (append L '(1)))
        )
        ;;; Checkers for any case that has a number for car
        ;;; of list. (cases like 2 x 3, 2 x, and  2)
        (  (AND
               (numberp (car L ))
               (eql (cadr L) 'x)
           )
               (cons 'G L)
        )
        ;;; Checks for negatve cases
        ( (eql (car L) '-)
            (list
                'U-
                (WFF (cadr L))
            )

         )
         ;;; Checks for sin cases
         ( (eql (car L) 'SIN)
            (list
                'SIN
                (WFF (cadr L))
            )
         )
         ;;; Checks for cos cases
         ( (eql (car L) 'COS)
            (list
                'COS
                (WFF (cadr L))
            )
         )
         ;;; Checks for addition (+) cases
         ;;; Cases like (2 x 3) + (2 x 3)
         ( (eql (cadr L) '+)
             (list
                 '+
                 (WFF (car L))
                 (WFF (caddr L))
             )
         )
         ;;; Checks for subtraction (-) cases.
         ;;; Cases like ( 2 x 3) - (3 x 5)
         ( (eql (cadr L) '-)
             (list
                 '-
                 (WFF (car L))
                 (WFF (caddr L))
             )
         )
         ;;;Checks for muliplication (*) cases.
         ;;; Cases like (2 x 4) * (3 x 5)
         ( (eql (cadr L) '*)
             (list
                 '*
                 (WFF (car L))
                 (WFF (caddr L))
             )
         )

         ;;; Checks for division cases (/) cases.
         ;;; Cases like (2 x 4) / (2 x 4)
         ( (eql (cadr L) '/)
             (list
                 '/
                 (WFF (car L))
                 (WFF (caddr L))
             )
         )
    )
)

;;;; Inserts an enrty in the hash table for specified
;;; atm and value.
(defun putp (atm ht value )
    (setf (gethash atm ht) value)
)

;;; Retuns the value for atm as the key in the hash table.
(defun getp (atm ht)
    (gethash atm ht)
)

;;; finds deriv of given expression (g)
(defun derg (expr)
    (list
         'G
         (* (car expr) (caddr expr))
         'X
         (- (caddr expr) 1)
    )
)

;;;Finds deriv of given expression (sum rule)
(defun der+ (expr)
    (cond ( (atom (car expr)) (der (cadr expr)) )
          ( (atom (cadr expr)) (der (car expr)) )
          (T
               (list
                    '+
                    (der(car expr))
                    (der (cadr expr))
                )
          )
     )
)

;;;Finds deriv of given expression (minus rule)
(defun der- (expr)
    (cond ( (eql (car expr) (cadr expr)) 0 )
          (T   (list
                    '-
                    (der (car expr))
                    (der (cadr expr))
               )
          )
    )
)

;;;Finds deriv of given expression (negative)
(defun derU- (expr)
    (cond ( (eql (car expr) 'U-) (der (cadadr L) ))
          ( T
             (list
                  'U-
                  (der (car expr))
             )
          )
    )
)
;;;Finds deriv of given expression (quotient rule)
(defun der/ (expr)
    (list
         '/
         (list
              '-
              (list
                   '*
                   (der (car expr))
                   (cadr expr)
              )
              (list
                   '*
                   (car expr)
                   (der (cadr expr))
              )
         )
         (list
              '*
              (cadr expr)
              (cadr expr)
         )
    )
)
;;;Find deriv of given expression (product rule)
(defun der* (expr)
    (list
         '+
         (list
              '*
              (der (car expr))
              (cadr expr)
         )
         (list
              '*
              (car expr)
              (der (cadr expr))
         )
    )
)
;;;finds deriv of given expression (cos)
(defun dercos (expr)
    (cond ( (eql (car expr) 'x)
                (list
                     'U-
                     (list
                          'sin
                          (car expr)
                     )
                 )
           )
           ( T   (list
                      '*
                      (list
                           'U-
                           (list
                                'sin
                                (car expr)
                                (der (car expr))
                           )
                       )
                  )
            )
    )
)
;;; Finds deriv of given expression (sin)
(defun dersin (expr)
    (cond ( (eql (car expr) 'x)
              (list
                   'cos
                   (car expr)
               )
           )
           ( T
                (list
                     '*
                     (list
                          'cos
                          (car expr)
                      )
                      (der (car expr))
                )
            )
     )
)


;;;Given a well formed forumla, it will find its derivative.
(defun der (L)
    (COND
        ;;; Checks for constants
        ( (numberp L) 0)
        ;;;( (atom  (cadr L)) L)
        ;;;Checks for cases like (G 2 x 1)
        ( (eql (cadddr L) '1)
            (cadr L)
        )
        ;;; Checks for all cases that begin with G
        ( (eql (car L ) 'G)
            (derg (cdr L))
        )
        ;;; Checks for addition (+) cases
        ( (eql (car L) '+ )
            (der+ (cdr L))
        )
        ;;; Checks for subtraction (-) cases
        ( (eql (car L) '-)
            (der- (cdr L))
        )
           ;;; (Checks for negative cases.
        ( (eql (car L) 'U-)
            (derU- (cdr L))
        )
        ;;;checks multiplication cases
        ( (eql (car L) '*)
            (der* (cdr L))
        )
        ;;; Checks for sin cases
        ( (eql (car L) 'sin)
            (dersin (cdr L))
        )
        ;;Checks for cos cases
        ( (eql (car L) 'cos)
            (dercos (cdr L))
        )
        ;;;Checks for division cases
        ( (eql (car L) '/)
            (der/ (cdr L))
        )
    )
)
