(define (find s predicate)
  (if (eq? s nil) #f 
    (if (predicate (car s)) (car s) (find (cdr-stream s) predicate)))
)

(define (scale-stream s k)
  (if (eq? s nil) nil 
    (cons-stream (* (car s) k) (scale-stream (cdr-stream s) k)))
)

(define (has-cycle s)
  (define (seen-stream k)
      (if (eq? k nil) #f 
      (if (eq? s (cdr-stream k)) #t 
        (seen-stream (cdr-stream k)))))
  (seen-stream s)
)


(define (has-cycle-constant s)
  'YOUR-CODE-HERE
)

