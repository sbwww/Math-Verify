import pytest
from tests.test_all import compare_strings


@pytest.mark.parametrize("gold, pred, expected", [
    (
        r"$(37,3,3,13),(17,3,3,7),(3,37,3,13),(3,17,3,7),(3,3,2,3)$",
        r"$\boxed{(3, 37, 3, 13), (3, 17, 3, 7), (3, 3, 2, 3), (3,17,3,7), (17,3,3,7), (37,3,3,13)}$",
        1,
    ),
    (
        r"$(p,q)=(3,2)$",
        r"$(3,2)$",
        1,
    ),
    (
        r"$(0;0;0),(0;-2;0),(0;0;6),(0;-2;6),(4;0;0),(4;-2;0),(4;0;6),(4;-2;6)$",
        r"\boxed{(4, 0, 6), (4, -2, 6), (0, 0, 6), (0, -2, 6), (4, 0, 0), (4, -2, 0), (0, 0, 0), (0, -2, 0)}",
        1,
    ),
    (
        r"$1\leq|z|\leq \frac{3}{2}$",
        r"$z \in \left[-\frac{3}{2}, -1\right] \cup \left[1, \frac{3}{2}\right]$",
        1,
    ),
    (
        r"$-12;-11;-10;-8;-7;-6$",
        r"$\boxed{\{-12, -11, -10, -8, -7, -6\}}$",
        1,
    ),
    (
        r"$AB=4,CD=5$",
        r"$\boxed{4, 5}$",
        1,
    ),
    (
        r"$(11,7)or(7,11)$",
        r"$\boxed{(7,11),\ (11,7)}$",
        1,
    ),
    (
        r"$S_{MBCN}:S=7:32$",
        r"$\boxed{7:32}$",
        1,
    ),
    (
        r"$\frac{NO}{BO}=\frac{1}{\sqrt{6}}$",
        r"$\frac{1}{\sqrt{6}}$",
        1,
    ),
    (
        r"$p=5,q=2;p=7,q=2$",
        r"$(5,2),(7,2)$",
        1,
    ),
    (
        r"$(p,q,r)=(3,2,7)$",
        r"$(3,2,7)$",
        1,
    ),
    (
        r"$V_{1}:V_{2}=11:21$",
        r"$11:21$",
        1,
    ),
    (
        r"$(2,1),(1,2),(-1,-20),(-20,-1)$",
        "solutions are:\n\n\\[\n\\boxed{(1, 2)}, \\boxed{(2, 1)}, \\boxed{(-1, -20)}, \\boxed{(-20, -1)}\n\\]",
        1,
    ),
    (
        r"\(\boxed{1}\) and \(\boxed{-2}\).",
        r"$\boxed{-2,1}$.",
        1,
    ),
    (
        r"$\text{odd}$",
        r"$odd$",
        1,
    ),
    (
        r"$\text{e}$",
        r"$e$",
        1,
    ),
    (
        r"$\text{E}$",
        r"$E$",
        1,
    ),
    (
        r"$d$",
        r"$\text{E}$",
        0
    ),
    (
        r"$1$ and $2$ and $3$",
        r"$\boxed{1,2,3}$",
        1
    ),
    (
        r"$(37,3,3,13),(17,3,3,7),(3,37,3,13),(3,17,3,7),(3,3,2,3)$",
        r"$\boxed{(3, 37, 3, 13), (3, 17, 3, 7), (3, 3, 2, 3), (3,17,3,7), (17,3,3,7), (37,3,3,13)}$",
        1,
    ),
    (
        r"$(37,3,3),(17,3,3,7),(3,37,3,13),(3,17,3,7),(3,3,2,3)$",
        r"$\boxed{(3, 37, 3, 13), (3, 17, 3, 7), (3, 3, 2, 3), (3,17,3,7), (17,3,3,7), (37,3,3,13)}$",
        0,
    ),
    (
        r"$(p,q)=(3,2)$",
        r"$\boxed{(3, 2)}$",
        1,
    ),
    (
        r"\boxed{x = -5,\ p = \frac{14}{3}} ",
        r"$\boxed{-5, \frac{14}{3}}$",
        1,
    ),
    (
        r"\boxed{a=4,\,-8,\,-10}",
        r"$\boxed{-10,-8,4}$",
        1,
    ),
    (
        r"\\boxed{W(n) = 1 \\text{ and } W(n) = -1",
        r"W(x)=1orW(x)=-1",
        1,
    ),
    (
        "$21,16$ or $11$",
        "$21,16,11$",
        1
    ),
    (
        r"\boxed{ p = 5, q = 2 \quad \text{and} \quad p = 7, q = 2}",
        r"$p=5,q=2;p=7,q=2$",
        1
    ),
    (
        r"\n\n\[ \boxed{p = -1 \text{ and } p = \dfrac{15}{8}} \]",
        r"$p=-1,p=\frac{15}{8}$",
        1
    ),
    (
        "$0<f(x)<1$",
        "$(0,1)$",
        1
    ),
    (
        r"\(\boxed{6 \text{ and } 8}\)",
        r"$\boxed{6,8}$",
        1
    ),
    (
        r"$\text{Even}$",
        r"$Even$",
        1
    )
    # (
    #     r"$f(x)$",
    #     r"$f(y)$",
    #     1
    # )
])
def test_numina_cases(gold, pred, expected):
    assert compare_strings(gold, pred, match_types=["latex", "expr"]) == expected