; 1D
(declare-const p Bool)
(declare-const q Bool)
(declare-const r Bool)
(push)

(assert (not (=> p q)))
(check-sat)
(get-model)

(pop)
; 2C
(push)

(define-fun conjecture () Bool
    (not (=> (or p q) p))
)

(push)
(assert conjecture)
(check-sat)
(pop)
(assert (not conjecture))
(check-sat)

(pop)
; 3B
(push)
(define-fun conjecture () Bool
    (and (and p (or q (not p))) (not q))
)
(echo "3: Check if true is possible")
(assert conjecture)
(check-sat)

(pop)
; 4A
(push)

(define-fun conjecture () Bool
    (= (not (or (not p) (not q) (not r))) (and p q r))
)
(echo "4: Check if false is possible")
(assert (not conjecture))
(check-sat)

(pop)
; 5C
(push)
(define-fun conjecture () Bool
    (and (not (or (not p) q)) (or p (not q)))
)
(echo "5: Check if true is possible")
(push)
(assert conjecture)
(check-sat)
(pop)
(echo "5: Check if false is possible")
(assert (not conjecture))
(check-sat)

(pop)
; 6C
(push)
(define-fun conjecture () Bool
    (not (or (and p q) (and (not p) (not q))))
)
(echo "6: Check if true is possible")
(push)
(assert conjecture)
(check-sat)
(pop)
(echo "6: Check if false is possible")
(assert (not conjecture))
(check-sat)

(pop)
; 7 A,B,C,D
(push)

(define-fun conjecture () Bool
    (or p (not p))
)
(define-fun implication() Bool
    (and (or (not p) p) (not p))
)

(echo "7: Check if false is possible")
(assert (not (=> implication conjecture)))
(check-sat)

(pop)
; 8 A,B,C,D
(push)
(define-fun conjecture () Bool
    (and p (not p))
)
(define-fun implication() Bool
    ;(or p (not p))
    ;(and p (not p))
    ;(or (and p (not q)) (not r))
    (and (or (not p) p) (not p))
)

(echo "8: Check if false is possible")
(assert (not (=> conjecture implication)))
(check-sat)

(pop)
; 9C
(push)

(define-fun conjecture () Bool
    (=> (=> p (=> q r)) (=> (=> p q) r))
)
(echo "9: Check if true is possible")
(push)
(assert conjecture)
(check-sat)
(pop)
(echo "9: Check if false is possible")
(assert (not conjecture))
(check-sat)

(pop)
; 10A
(push)

(define-fun conjecture () Bool
    (=> (=> (=> p q) r) (=> p (=> q r)))
)
(echo "10: Check if true is possible")
(push)
(assert conjecture)
(check-sat)
(pop)
(echo "10: Check if false is possible")
(assert (not conjecture))
(check-sat)

