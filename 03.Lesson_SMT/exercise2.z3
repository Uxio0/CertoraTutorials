(declare-const p Bool)
(declare-const q Bool)

(define-fun conjecture () Bool
    (= (and p q) p)
)

(define-fun conjecture2 () Bool
    (=> p q)
)

; Prove by denying the premise

(assert (not (= conjecture conjecture2)))
(check-sat)
