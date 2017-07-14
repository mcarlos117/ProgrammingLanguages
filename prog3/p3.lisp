;;; Project 3

;;; Passes a variable which it increments and assigns as the new value.
(defmacro ++ (numval)
    `(setf ,numval (+ 1 ,numval))
)

;;; Passes a control variable, begin variable, end value, and body.
;;; The result should iterate and print with the given values.
(defmacro iterate (contvar begval endval &rest body)
    (let ((g (gensym)))
        `( do ( (,contvar ,begval (+ ,contvar 1))(,g ,endval) )
              ( (> ,contvar ,g) T )
                  ,@body
         )
    )
)

