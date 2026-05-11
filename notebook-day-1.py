import marimo

__generated_with = "0.20.4"
app = marimo.App()


@app.cell
def _():
    import marimo as mo

    return (mo,)


@app.cell(hide_code=True)
def _(mo):
    mo.md("""
    # Redstart: A Lightweight Reusable Booster
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.image(src="public/images/redstart.png")
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    Project Redstart is an attempt to design the control systems of a reusable booster during landing.
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    In principle, it is similar to SpaceX's Falcon Heavy Booster.

    >The Falcon Heavy booster is the first stage of SpaceX's powerful Falcon Heavy rocket, which consists of three modified Falcon 9 boosters strapped together. These boosters provide the massive thrust needed to lift heavy payloads—like satellites or spacecraft—into orbit. After launch, the two side boosters separate and land back on Earth for reuse, while the center booster either lands on a droneship or is discarded in high-energy missions.
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.center(
        mo.Html("""
    <iframe width="560" height="315" src="https://www.youtube.com/embed/RYUr-5PYA7s?si=EXPnjNVnqmJSsIjc" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share" referrerpolicy="strict-origin-when-cross-origin" allowfullscreen></iframe>""")
    )
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ## Dependencies
    """)
    return


@app.cell
def _():
    import scipy
    import scipy.integrate as sci

    import matplotlib as mpl
    import matplotlib.pyplot as plt

    import numpy as np
    import numpy.linalg as la

    return np, plt, sci


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ## The Model

    The Redstart booster in model as a rigid tube of length $\ell$ and negligible diameter whose mass $M$ is uniformly spread along its length. It may be located in 2D space by the coordinates $(x, y)$ of its center of mass and the angle $\theta$ it makes with respect to the vertical (with the convention that $\theta > 0$ for a left tilt, i.e. the angle is measured counterclockwise)

    This booster has an orientable reactor at its base ; the force that it generates is of amplitude $f \geq 0$ and the angle of the force with respect to the booster axis is $\phi$ (with a counterclockwise convention).

    We assume that the booster is subject to gravity, the reactor force and that the friction of the air is negligible.
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.center(mo.image(src="public/images/geometry.svg"))
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ## Constants

    For the sake of simplicity (this is merely a toy model!) in the sequel we assume that:

    - the total length $\ell$ of the booster is 2 meters,
    - its mass $M$ is 1 kg,
    - the gravity constant $g$ is 1 m/s^2.

    This set of values is completely unrealistic, but very simple! It will simplify our computations and will not fundamentally impact the structure of the booster dynamics.
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    # Getting Started
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ## 🧩 Constants

    Define the Python constants `g`, `M` and `l` that correspond to the gravity constant, the mass and half-length of the booster.
    """)
    return


@app.cell
def _():
    g = 1.0 
    M = 1.0 
    l = 1.0 
    return M, g, l


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ## 🧩 Forces

    Compute the cartesian coordinates $f_x$ and $f_y$ of the force applied to the booster by the reactor, functions of $f$, $\theta$ and $\phi$.
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    **Formule.** L'axe du booster est incliné de $\theta$ par rapport à la verticale (CCW positif). La force réacteur fait un angle $\phi$ supplémentaire (CCW) avec cet axe, donc un angle total $\theta + \phi$ avec la verticale :

    $$
    \boxed{\;f_x = -f\sin(\theta + \phi), \qquad f_y = +f\cos(\theta + \phi)\;}
    $$

    *Vérifications :* si $\theta = \phi = 0$, alors $(f_x, f_y) = (0, f)$ — poussée verticale vers le haut.
    Si $\theta = 0,\ \phi = \pi/2$, alors $(f_x, f_y) = (-f, 0)$ — poussée horizontale vers la gauche.
    """)
    return


@app.cell
def _(np):
    def reactor_force_components(f: float, theta: float, phi: float):

        fx = -f * np.sin(theta + phi)
        fy = f * np.cos(theta + phi)
        return fx, fy


    return (reactor_force_components,)


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ## 🧩 Center of Mass

    Give the ordinary differential equation that governs the evolution of the position $(x, y)$ of the center of mass of the booster.
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    **Équation.** Le booster subit deux forces : le réacteur $(f_x, f_y)$ et le poids $(0, -Mg)$. La deuxième loi de Newton appliquée au centre de masse donne :

    $$
    M\ddot{x} = f_x, \qquad M\ddot{y} = f_y - Mg
    $$

    soit, en remplaçant par l'expression de $(f_x, f_y)$ :

    $$
    \boxed{\;\ddot{x} = -\dfrac{f}{M}\sin(\theta + \phi), \qquad \ddot{y} = \dfrac{f}{M}\cos(\theta + \phi) - g\;}
    $$
    """)
    return


@app.cell
def _(M, g, reactor_force_components):
    # dynamique du centre de masse (deuxième loi de newton)
    #   x¨ = fx/M
    #   y¨ = fy/M - g
    def com_acceleration(f: float, theta: float, phi: float):
        fx, fy = reactor_force_components(f, theta, phi)
        ax = fx / M
        ay = fy / M - g
        return ax, ay


    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ## 🧩 Moment of inertia

    Compute the [moment of inertia](https://en.wikipedia.org/wiki/Moment_of_inertia) $J$ of the booster and define the corresponding Python variable `J`.
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    **Calcul.** Le booster est une tige homogène de masse $M$ et de longueur totale $2\ell$. La densité linéique vaut $\lambda = M / (2\ell)$. Le moment d'inertie autour du centre de masse est :

    $$
    J = \int_{-\ell}^{\ell} \lambda\, r^2\, dr
      = \frac{M}{2\ell} \cdot \left[\frac{r^3}{3}\right]_{-\ell}^{\ell}
      = \frac{M}{2\ell} \cdot \frac{2\ell^3}{3}
      = \boxed{\;\frac{M\ell^2}{3}\;}
    $$

    soit, sous la forme standard du barreau de longueur $L = 2\ell$ : $J = \dfrac{1}{12} M L^2 = \dfrac{1}{12} M (2\ell)^2$.
    """)
    return


@app.cell
def _(M, l):

    J = (1.0 / 12.0) * M * (2.0 * l) ** 2  # = (1/3) M l^2
    J
    return (J,)


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ## 🧩 Tilt

    Give the ordinary differential equation that governs the evolution of the tilt angle $\theta$.
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    **Calcul du couple.** Dans le repère du booster, le réacteur est situé à la base, en position $\mathbf{r} = (0,\, -\ell)$, et la force réacteur vaut $\mathbf{F}_{\text{body}} = f\,(-\sin\phi,\ \cos\phi)$.

    Le couple autour du centre de masse est la composante $z$ du produit vectoriel $\mathbf{r}\times\mathbf{F}$ :

    $$
    \tau \;=\; r_x F_y - r_y F_x
          \;=\; 0\cdot f\cos\phi \;-\; (-\ell)\cdot(-f\sin\phi)
          \;=\; -\ell f \sin\phi.
    $$

    L'équation du mouvement angulaire $J\ddot\theta = \tau$ donne donc :

    $$
    \boxed{\;\ddot{\theta} = -\dfrac{\ell\, f}{J}\sin\phi\;}
    $$

    *Remarques :* si $\phi = 0$ (poussée alignée avec l'axe du booster), $\ddot\theta = 0$ — pas de couple, le tilt est conservé. Le signe est cohérent : $\phi > 0$ pousse la base vers la gauche, donc fait basculer le sommet vers la droite ($\theta$ diminue).
    """)
    return


@app.cell
def _(J, l, np):
    # Le bras de levier du réacteur est l (demi-longueur).
    # Couple autour du centre de masse : tau = -l * f * sin(phi)
    # Equation d'évolution du tilt :  J * theta_ddot = -l * f * sin(phi)
    def tilt_acceleration(f: float, phi: float):
        return -l * f * np.sin(phi) / J


    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ## 🧩 Vector Field

    Denote

    - $v_x =\dot{x}$, $v_y = \dot{y}$ the components of the booster center of mass velocity,
    - $\omega = \dot{\theta}$ the angular velocity of the booster.


    What is is dimension $n$ of the state space?
    What is the state $s \in \R^n$ of the booster dynamics?
    Provide the definition of the function $F : \mathbb{R}^{n + 2} \to \mathbb{R}^n$ such that the system evolves
    according to

    $$
    \dot{s} = F(s, f, \phi).
    $$
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    **Réponse.** L'état est de dimension $n = 6$ :

    $$
    s = (x,\; v_x,\; y,\; v_y,\; \theta,\; \omega) \in \mathbb{R}^6
    $$

    et

    $$
    F(s, f, \phi) =
    \begin{pmatrix}
    v_x \\
    -\dfrac{f}{M}\sin(\theta + \phi) \\
    v_y \\
    \dfrac{f}{M}\cos(\theta + \phi) - g \\
    \omega \\
    -\dfrac{\ell\, f}{J}\sin(\phi)
    \end{pmatrix}.
    $$
    """)
    return


@app.cell
def _(J, M, g, l, np):
    def F(s, f, phi):
        x, vx, y, vy, theta, omega = s
        ax = -f * np.sin(theta + phi) / M
        ay = f * np.cos(theta + phi) / M - g
        alpha = -l * f * np.sin(phi) / J
        return np.array([vx, ax, vy, ay, omega, alpha])


    return (F,)


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ## 🧩 Simulation

    Define a function `redstart_solve` that, given the input parameters:

    - `t_span`: a pair of initial time `t_0` and final time `t_f`,
    - `y0`: the value of `[x, vx, y, vy, theta, omega]` at `t_0`,
    - `f_phi`: a function that given the current time `t` and current state value `y`
         returns the values of the inputs `f` and `phi` in an array.

    returns:

    - `sol`: a function that given a time `t` returns the value of `[x, vx, y, vy, theta, omega]` at time `t` (and that also accepts 1d-arrays of times for multiple state evaluations).

    A typical usage would be:

    ```python
    def free_fall_example():
        t_span = [0.0, 5.0]
        y0 = [0.0, 0.0, 10.0, 0.0, 0.0, 0.0] # [x, vx, y, vy, theta, omega]
        def f_phi(t, y):
            return np.array([0.0, 0.0]) # [f, phi]
        sol = redstart_solve(t_span, y0, f_phi)
        t = np.linspace(t_span[0], t_span[1], 1000)
        y_t = sol(t)[2]
        plt.plot(t, y_t, label=r"$y(t)$ (height in meters)")
        plt.plot(t, l * np.ones_like(t), color="grey", ls="--", label=r"$y=\ell$")
        plt.title("Free Fall")
        plt.xlabel("time $t$")
        plt.grid(True)
        plt.legend()
        return plt.gcf()
    free_fall_example()
    ```
    """)
    return


@app.cell
def _(F, sci):
    def redstart_solve(t_span, y0, f_phi):
        def rhs(t, s):
            f, phi = f_phi(t, s)
            return F(s, f, phi)

        result = sci.solve_ivp(
            rhs, t_span, y0, dense_output=True, rtol=1e-8, atol=1e-10
        )
        return result.sol


    return (redstart_solve,)


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ## 🧩 Freefall test


    In the `free_fall` example scenario. scenario, at what moment should the center of mass of the booster theoretically cross the
    height of $y = \ell$?

    Check your `redstart_solve` function in this scenario and produce a graph that allows us to check the above answer numerically/visually.
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    **Solution analytique.** En chute libre, $\ddot{y} = -g$ d'où

    $$
    y(t) = y_0 - \tfrac{1}{2} g t^2 = 10 - \tfrac{1}{2} t^2.
    $$

    On cherche $t^\star$ tel que $y(t^\star) = \ell = 1$ :

    $$
    t^\star = \sqrt{\dfrac{2(y_0 - \ell)}{g}} = \sqrt{18} \approx 4.243\ \text{s}.
    $$
    """)
    return


@app.cell
def _(g, l, np, plt, redstart_solve):
    def free_fall_example():
        t_span = [0.0, 5.0]
        y0 = [0.0, 0.0, 10.0, 0.0, 0.0, 0.0]

        def f_phi(t, y):
            return np.array([0.0, 0.0])

        sol = redstart_solve(t_span, y0, f_phi)
        t = np.linspace(t_span[0], t_span[1], 1000)
        y_t = sol(t)[2]
        t_star = np.sqrt(2 * (10.0 - l) / g)

        plt.figure()
        plt.plot(t, y_t, label=r"$y(t)$ (height in meters)")
        plt.plot(t, l * np.ones_like(t), color="grey", ls="--", label=r"$y=\ell$")
        plt.axvline(
            t_star,
            color="red",
            ls=":",
            label=fr"$t^\star = \sqrt{{18}} \approx {t_star:.3f}$ s",
        )
        plt.title("Free Fall")
        plt.xlabel("time $t$")
        plt.grid(True)
        plt.legend()
        return plt.gcf()


    free_fall_example()
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ## 🧩 Controlled Landing

    Assume that $x$, $\dot{x}$, $\theta$ and $\dot{\theta}$ are null at $t=0$ and that $y(0)= 10$ and $\dot{y}(0) = - 2$.

    Find a time-varying force $f(t)$ which, when applied in the booster axis ($\theta=0$), yields $y(5)=\ell / 2 = 1$ (the booster is at ground level) and $\dot{y}(5)=0$ (the booster is at rest).

    Simulate the corresponding scenario, display graphically the results and check that your solution works as expected.
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    **Approche.** Avec $\theta \equiv 0$ et $\phi \equiv 0$, on a $\ddot{y} = f/M - g$.
    On choisit donc une trajectoire $y(t)$ polynomiale qui satisfait les conditions
    aux bords.

    On ajoute donc les contraintes $\ddot{y}(0) = -g$ (i.e. $f(0)=0$) et
    $\ddot{y}(T) = 0$ (i.e. $f(T)=Mg$ : hover en fin de course), ce qui mène à un
    polynôme de degré 5 — et $f$ reste positif sur tout l'intervalle.

    On déduit alors la commande :
    $$
    f(t) = M\bigl(\ddot{y}(t) + g\bigr), \qquad \phi(t) = 0.
    $$
    """)
    return


@app.cell
def _(M, g, l, np, plt, redstart_solve):
    def controlled_landing_example():
        T = 5.0
        # contraintes : y(0)=10, y'(0)=-2, y''(0)=-g  et  y(T)=l, y'(T)=0, y''(T)=0
        # (l Python = demi-longueur = ℓ/2 énoncé)
        a0, a1, a2 = 10.0, -2.0, -g / 2.0  # car y(t) = sum a_k t^k => y''(0) = 2*a2
        rhs = np.array(
            [
                l - a0 - a1 * T - a2 * T**2,
                0.0 - a1 - 2 * a2 * T,
                0.0 - 2 * a2,
            ]
        )
        A = np.array(
            [
                [T**3, T**4, T**5],
                [3 * T**2, 4 * T**3, 5 * T**4],
                [6 * T, 12 * T**2, 20 * T**3],
            ]
        )
        a3, a4, a5 = np.linalg.solve(A, rhs)

        def y_ddot(t):
            return 2 * a2 + 6 * a3 * t + 12 * a4 * t**2 + 20 * a5 * t**3

        def f_phi(t, s):
            f = M * (y_ddot(t) + g)
            return np.array([f, 0.0])

        t_span = [0.0, T]
        y0 = [0.0, 0.0, 10.0, -2.0, 0.0, 0.0]
        sol = redstart_solve(t_span, y0, f_phi)

        t = np.linspace(t_span[0], t_span[1], 1000)
        ys = sol(t)
        f_t = np.array([f_phi(ti, None)[0] for ti in t])

        fig, axes = plt.subplots(3, 1, figsize=(8, 9), sharex=True)
        axes[0].plot(t, ys[2], label=r"$y(t)$")
        axes[0].axhline(l, color="grey", ls="--", label=r"$y = \ell/2$")
        axes[0].set_ylabel("y (m)")
        axes[0].legend()
        axes[0].grid(True)

        axes[1].plot(t, ys[3], label=r"$\dot{y}(t)$", color="tab:orange")
        axes[1].axhline(0.0, color="grey", ls="--")
        axes[1].set_ylabel(r"$\dot{y}$ (m/s)")
        axes[1].legend()
        axes[1].grid(True)

        axes[2].plot(t, f_t, label=r"$f(t)$", color="tab:green")
        axes[2].axhline(M * g, color="grey", ls="--", label=r"$Mg$")
        axes[2].set_ylabel("f (N)")
        axes[2].set_xlabel("time t (s)")
        axes[2].legend()
        axes[2].grid(True)

        fig.suptitle(
            f"Controlled landing : y(T)={ys[2][-1]:.4f},  $\\dot{{y}}$(T)={ys[3][-1]:.4f}"
        )
        fig.tight_layout()
        return fig


    controlled_landing_example()
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    # Animations

    It's very handy to visualize the evolution of our booster "as a movie"!

    Have a look at the [animations tutorial] to understand the basics of animated SVG documents.

    [animations tutorial]: http://localhost:2718/?file=animations.py
    """)
    return


@app.cell
def _():
    from svg import svg, transform, animate_transform

    return animate_transform, svg, transform


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ## 🧩 Environment

    Create a function `world` whose arguments are:

    - `view_box`: a view box in cartesian coordinates `[x_min, x_max, y_min, y_max]`,

    - `*objects`: (optional) list of extra svg elements (default : `[]`).

    and that returns a SVG string which

    - has the appropriate cartesian view box and frame ($y$-axis upwards),

    - depicts the sky and the ground,

    - depicts a 2 meter wide green ground target centered on $(0, 0)$,

    - displays the objects (if any) inserted on top of the world.

    Test your function with the following scenes:

    ```python
    mo.hstack(
        [
            # Display an empty world
            mo.Html(
                world([-3, 3, -2, 4])
            ),
            # Display a world with a black square on top of the landing pad
            mo.Html(
                world(
                    [-3, 3, -2, 4],
                    svg.rect(x=-1, y=0, width=2, height=2, fill="black"),
                )
            ),
            # Display a world with a red square in the top-left corner of the view box
            # and a blue square on the top-right corner of the view box.
            mo.Html(
                world(
                    [-3, 3, -2, 4],
                    svg.rect(x=-3, y=2, width=2, height=2, fill="red"),
                    svg.rect(x=1, y=2, width=2, height=2, fill="blue"),
                )
            )
        ],
        justify="space-around"
    )
    ```
    """)
    return


@app.cell
def _(svg, transform):
    def world(view_box, *objects):
        x_min, x_max, y_min, y_max = view_box
        width = x_max - x_min
        height = y_max - y_min
        sky_top = max(0.0, y_max)
        ground_bottom = min(0.0, y_min)
        # Ordre de tracé : ciel -> objets -> sol -> pad.
        # Le sol étant dessiné APRES les objets, il masque visuellement
        # toute portion d'objet située sous y = 0 (la fusée ne traverse plus le sol).
        return svg.svg(
            viewBox=f"0 0 {width} {height}",
            xmlns="http://www.w3.org/2000/svg",
        )(
            transform.translate(x=-x_min, y=y_max)(
                transform.scale(x=1, y=-1)(
                    svg.rect(
                        x=x_min, y=0, width=width, height=sky_top, fill="#87CEEB"
                    ),
                    *objects,
                    svg.rect(
                        x=x_min,
                        y=ground_bottom,
                        width=width,
                        height=-ground_bottom,
                        fill="#8B6F47",
                    ),
                    svg.rect(x=-1, y=-0.05, width=2, height=0.1, fill="#2E8B57"),
                )
            )
        )


    return (world,)


@app.cell
def _(mo, svg, world):
    mo.hstack(
        [
            mo.Html(world([-3, 3, -2, 4])),
            mo.Html(
                world(
                    [-3, 3, -2, 4],
                    svg.rect(x=-1, y=0, width=2, height=2, fill="black"),
                )
            ),
            mo.Html(
                world(
                    [-3, 3, -2, 4],
                    svg.rect(x=-3, y=2, width=2, height=2, fill="red"),
                    svg.rect(x=1, y=2, width=2, height=2, fill="blue"),
                )
            ),
        ],
        justify="space-around",
    )
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ## 🧩 Booster Drawing

    Create a `booster` function that:

    - takes the numeric arguments `x`, `y`, `theta` (in radians), `f` and `phi` (in radians)

    and returns

    - a SVG fragment that represents the body of the booster and the flame of its reactor.
    (The booster drawing can be very simple, for example a rectangle for the body and another one of a different color for the flame will be fine.)

    **Constraint:** make sure that

    - the orientation of the flame is correct,
    - its length is proportional to the force $f$,
    - the flame length is equal to $\ell/2$ when $f=Mg$.


    Test you function in the following scenarios:

    ```python
    mo.hstack(
        [
            mo.Html(
                world(
                    [-3, 3, -2, 4],
                    booster(0, l/2, 0, 0, 0),
                )
            ),
            mo.Html(
                world(
                    [-3, 3, -2, 4],
                    booster(0, l, 0, M * g, 0),
                )
            ),
            mo.Html(
                world(
                    [-3, 3, -2, 4],
                    booster(-l/2, l, np.pi / 4, 2 * M * g, np.pi / 2),
                )
            ),
        ],
        justify="space-around",
    )
    ```
    """)
    return


@app.cell
def _(M, g, l, np, svg, transform):
    BODY_WIDTH = 0.2
    FLAME_WIDTH = 0.15


    def booster(x, y, theta, f, phi):
        # Longueur de flamme : proportionnelle à f, vaut l/2 (≈ 1/4 du corps) quand f = M*g.
        flame_length = (f / (M * g)) * (l / 2.0)
        theta_deg = float(np.degrees(theta))
        phi_deg = float(np.degrees(phi))

        body = svg.rect(
            x=-BODY_WIDTH / 2.0,
            y=-l,
            width=BODY_WIDTH,
            height=2.0 * l,
            fill="black",
        )
        # En repère booster, la flamme sort à la base (0, -l) opposée à la force.
        # Pour phi=0, force = (0, +f) (axe booster vers le haut), flamme vers le bas.
        flame = transform.rotate(a=phi_deg, x=0, y=-l)(
            svg.rect(
                x=-FLAME_WIDTH / 2.0,
                y=-l - flame_length,
                width=FLAME_WIDTH,
                height=flame_length,
                fill="orangered",
            )
        )
        return transform.translate(x=x, y=y)(
            transform.rotate(a=theta_deg)(body, flame)
        )


    return BODY_WIDTH, FLAME_WIDTH, booster


@app.cell
def _(M, booster, g, l, mo, np, world):
    mo.hstack(
        [
            mo.Html(world([-3, 3, -2, 4], booster(0, l / 2, 0, 0, 0))),
            mo.Html(world([-3, 3, -2, 4], booster(0, l, 0, M * g, 0))),
            mo.Html(
                world(
                    [-3, 3, -2, 4],
                    booster(-l / 2, l, np.pi / 4, 2 * M * g, np.pi / 2),
                )
            ),
        ],
        justify="space-around",
    )
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ## 🧩 Booster Animation

    Create a `booster_anim` function whose arguments are:

    - `x`, `y`, `theta` (in radians), `f` and `phi` (in radians)
    **which are functions of a time `t`**.
    - an animation duration `T`,

    and returns

    - a SVG fragment that represents the animated body of the booster and the flame of its reactor during `T` seconds, then repeats.
    (The booster drawing can be very simple, for example a rectangle for the body and another one of a different color for the flame will be fine.)

    **Constraint:** make sure that

    - the orientation of the flame is correct,
    - its length is proportional to the force $f$,
    - the flame length is equal to $\ell/2$ when $f=Mg$.

    Test your function in the following scenario:

    ```python
    def booster_anim_0():
        T = 5.0
        def x(t):
            return -l/2 + l * (t / T)
        def y(t):
            return l/2 + l/2 * (t / T)
        def theta(t):
            return (t / T) * 2 * np.pi
        def f(t):
            return M * g * (t / T)
        def phi(t):
            return 2 * np.pi * (t / T)
        return booster_anim(x, y, theta, f, phi, T=T)

    mo.Html(
        world([-3, 3, -2, 4], booster_anim_0())
    ).center()
    ```
    """)
    return


@app.cell
def _(BODY_WIDTH, FLAME_WIDTH, M, animate_transform, g, l, np, svg, transform):
    def booster_anim(x, y, theta, f, phi, T, fps=30.0):
        def flame_length(t):
            return (f(t) / (M * g)) * (l / 2.0)

        def theta_deg(t):
            return float(np.degrees(theta(t)))

        def phi_deg(t):
            return float(np.degrees(phi(t)))

        body = svg.rect(
            x=-BODY_WIDTH / 2.0,
            y=-l,
            width=BODY_WIDTH,
            height=2.0 * l,
            fill="black",
        )
        unit_flame = svg.rect(
            x=-FLAME_WIDTH / 2.0,
            y=-1.0,
            width=FLAME_WIDTH,
            height=1.0,
            fill="orangered",
        )
        flame = transform.translate(x=0, y=-l)(
            animate_transform.rotate(a=phi_deg, T=T, fps=fps)(
                animate_transform.scale(x=1.0, y=flame_length, T=T, fps=fps)(
                    unit_flame
                )
            )
        )
        return animate_transform.translate(x=x, y=y, T=T, fps=fps)(
            animate_transform.rotate(a=theta_deg, T=T, fps=fps)(body, flame)
        )


    return (booster_anim,)


@app.cell
def _(M, booster_anim, g, l, mo, np, world):
    def booster_anim_0():
        T = 5.0

        def x(t):
            return -l / 2 + l * (t / T)

        def y(t):
            return l / 2 + l / 2 * (t / T)

        def theta(t):
            return (t / T) * 2 * np.pi

        def f(t):
            return M * g * (t / T)

        def phi(t):
            return 2 * np.pi * (t / T)

        return booster_anim(x, y, theta, f, phi, T=T)


    mo.Html(world([-3, 3, -2, 4], booster_anim_0())).center()
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ## 🧩 Animated Simulation Results

    Let's go back to a booster whose evolution is governed by its system of ordinary differentential equations. Produce a animation of the booster for 5 seconds for each of the following initial value problems:

    1. $(x, \dot{x}, y, \dot{y}, \theta, \dot{\theta}) = (0.0, 0.0, 10.0, 0.0, 0.0, 0.0)$, $f=0$ and $\phi=0$

    2. $(x, \dot{x}, y, \dot{y}, \theta, \dot{\theta}) = (0.0, 0.0, 10.0, 0.0, 0.0, 0.0)$, $f=Mg$ and $\phi=0$

    3. $(x, \dot{x}, y, \dot{y}, \theta, \dot{\theta}) = (0.0, 0.0, 10.0, 0.0, 0.0, 0.0)$, $f=Mg$ and $\phi=\pi/8$

    4. The "controlled landing" scenario (see above).
    """)
    return


@app.cell
def _(booster_anim, np, redstart_solve, world):
    SCENARIO_VIEW = [-5, 5, -3, 12]
    SCENARIO_T = 5.0


    def animate_scenario(y0, f_phi_law, T=SCENARIO_T, view_box=SCENARIO_VIEW):
        sol = redstart_solve([0.0, T], y0, f_phi_law)

        def x_t(t):
            return float(sol(t)[0])

        def y_t(t):
            return float(sol(t)[2])

        def theta_t(t):
            return float(sol(t)[4])

        def f_t(t):
            return float(f_phi_law(t, sol(t))[0])

        def phi_t(t):
            return float(f_phi_law(t, sol(t))[1])

        return world(
            view_box, booster_anim(x_t, y_t, theta_t, f_t, phi_t, T=T)
        )


    Y0_FALL = [0.0, 0.0, 10.0, 0.0, 0.0, 0.0]


    def const_law(f, phi):
        def f_phi_law(t, s):
            return np.array([f, phi])

        return f_phi_law


    return Y0_FALL, animate_scenario, const_law


@app.cell
def _(Y0_FALL, animate_scenario, const_law, mo):
    mo.md("### 1. Free fall ($f = 0$, $\\phi = 0$)")
    mo.Html(animate_scenario(Y0_FALL, const_law(0.0, 0.0))).center()
    return


@app.cell
def _(M, Y0_FALL, animate_scenario, const_law, g, mo):
    mo.md("### 2. Hover ($f = Mg$, $\\phi = 0$)")
    mo.Html(animate_scenario(Y0_FALL, const_law(M * g, 0.0))).center()
    return


@app.cell
def _(M, Y0_FALL, animate_scenario, const_law, g, mo, np):
    mo.md("### 3. Tilted thrust ($f = Mg$, $\\phi = \\pi/8$)")
    mo.Html(animate_scenario(Y0_FALL, const_law(M * g, np.pi / 8))).center()
    return


@app.cell
def _(M, animate_scenario, g, l, mo, np):
    def controlled_landing_law():
        T = 5.0
        a0, a1, a2 = 10.0, -2.0, -g / 2.0
        rhs = np.array(
            [
                l - a0 - a1 * T - a2 * T**2,
                0.0 - a1 - 2 * a2 * T,
                0.0 - 2 * a2,
            ]
        )
        A = np.array(
            [
                [T**3, T**4, T**5],
                [3 * T**2, 4 * T**3, 5 * T**4],
                [6 * T, 12 * T**2, 20 * T**3],
            ]
        )
        a3, a4, a5 = np.linalg.solve(A, rhs)

        def y_ddot(t):
            return 2 * a2 + 6 * a3 * t + 12 * a4 * t**2 + 20 * a5 * t**3

        def f_phi_law(t, s):
            return np.array([M * (y_ddot(t) + g), 0.0])

        return f_phi_law


    mo.md("### 4. Controlled landing")
    mo.Html(
        animate_scenario(
            [0.0, 0.0, 10.0, -2.0, 0.0, 0.0],
            controlled_landing_law(),
        )
    ).center()
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ## 🧩 Tilted Controlled Landing

    On veut maintenant que la fusée démarre **inclinée** ($\theta(0) = \theta_0 \neq 0$) et **se redresse au cours de la descente** pour finir verticale au-dessus du pad ($\theta(T) \approx 0$ **et** $x(T) \approx 0$).

    Avec seulement deux entrées $(f, \phi)$ on ne peut pas suivre indépendamment une trajectoire $\theta_\text{des}(t)$ *et* contrôler $x(t)$ (l'effort latéral et le couple sont liés via $\phi$). On utilise donc un **retour d'état** (state feedback) sur la dynamique latérale.

    **Linéarisation autour du vol stationnaire** ($\theta=0$, $\phi=0$, $f=Mg$). Avec $\sin\alpha \approx \alpha$, $\cos\alpha \approx 1$ :

    $$
    \begin{aligned}
    \ddot{x} &\approx -g\,(\theta + \phi),\\
    \ddot{\theta} &\approx -\dfrac{\ell M g}{J}\,\phi.
    \end{aligned}
    $$

    Avec l'état latéral $\xi = (x,\ \dot x,\ \theta,\ \omega)^\top$ et l'entrée $\phi$ :

    $$
    \dot\xi = A\xi + B\phi, \qquad
    A = \begin{pmatrix} 0 & 1 & 0 & 0 \\ 0 & 0 & -g & 0 \\ 0 & 0 & 0 & 1 \\ 0 & 0 & 0 & 0 \end{pmatrix},\qquad
    B = \begin{pmatrix} 0 \\ -g \\ 0 \\ -\ell M g / J \end{pmatrix}.
    $$

    **Loi de commande.** On place les pôles de $A - BK$ par `scipy.signal.place_poles` (pôles autour de $-1.2$) puis on applique $\phi = -K\xi$. Pour la composante verticale on garde la compensation :

    $$
    f = \dfrac{M(\ddot y_\text{des} + g)}{\cos(\theta + \phi)}.
    $$

    **Saturation.** Comme $\theta_0 = 30°$ est grand, $-K\xi$ peut dépasser $60°$ au démarrage. Au lieu de borner $|\phi|$ (qui ferait passer $\theta+\phi$ près de $\pi/2$ et exploser le $\cos$), on borne directement $|\theta + \phi| \leq 85°$ — la singularité est évitée et le contrôleur peut commander des $\phi$ plus grands sans risque.

    Le gain $K$ est calculé une fois pour toutes au démarrage. Cette structure ramène $(x, \dot x, \theta, \omega) \to 0$ tout en suivant la trajectoire verticale planifiée.
    """)
    return


@app.cell
def _(J, M, g, l, np):
    import scipy.signal as _sig

    def tilted_landing_law(theta_0, pole=1.2):
        T = 5.0
        a0_y, a1_y, a2_y = 10.0, -2.0, -g / 2.0
        A_y = np.array(
            [
                [T**3, T**4, T**5],
                [3 * T**2, 4 * T**3, 5 * T**4],
                [6 * T, 12 * T**2, 20 * T**3],
            ]
        )
        rhs_y = np.array(
            [
                l - a0_y - a1_y * T - a2_y * T**2,
                0.0 - a1_y - 2 * a2_y * T,
                0.0 - 2 * a2_y,
            ]
        )
        a3_y, a4_y, a5_y = np.linalg.solve(A_y, rhs_y)

        def y_ddot(t):
            return 2 * a2_y + 6 * a3_y * t + 12 * a4_y * t**2 + 20 * a5_y * t**3

        # Linéarisation latérale autour de (theta=0, phi=0, f=Mg) et placement de pôles
        A_lin = np.array(
            [
                [0.0, 1.0, 0.0, 0.0],
                [0.0, 0.0, -g, 0.0],
                [0.0, 0.0, 0.0, 1.0],
                [0.0, 0.0, 0.0, 0.0],
            ]
        )
        B_lin = np.array([[0.0], [-g], [0.0], [-l * M * g / J]])
        poles = [-pole, -pole * 1.05, -pole * 1.10, -pole * 1.15]
        K = _sig.place_poles(A_lin, B_lin, poles).gain_matrix.flatten()
        # Saturation : borne |theta + phi| <= 85° pour éviter la singularité de cos
        ALPHA_MAX = np.radians(85.0)

        def f_phi_law(t, s):
            if s is None:
                return np.array([M * (y_ddot(t) + g), 0.0])
            x, vx, theta, om = s[0], s[1], s[4], s[5]
            phi = float(-K[0] * x - K[1] * vx - K[2] * theta - K[3] * om)
            phi = float(np.clip(phi, -ALPHA_MAX - theta, ALPHA_MAX - theta))
            denom = np.cos(theta + phi)
            if abs(denom) < 1e-3:
                return np.array([0.0, 0.0])
            f = M * (y_ddot(t) + g) / denom
            if f < 0.0:
                f = 0.0
            return np.array([f, phi])

        return f_phi_law


    return (tilted_landing_law,)


@app.cell
def _(animate_scenario, mo, np, tilted_landing_law):
    THETA_0 = np.pi / 6  # 30 degres
    mo.md(rf"### 5. Tilted controlled landing ($\theta_0 = \pi/6 \approx 30^\circ$)")
    mo.Html(
        animate_scenario(
            [0.0, 0.0, 10.0, -2.0, THETA_0, 0.0],
            tilted_landing_law(THETA_0),
        )
    ).center()
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ## 🧩 Off-center Tilted Controlled Landing

    Même contrôleur que ci-dessus (placement de pôles sur la dynamique latérale linéarisée), mais avec une condition initiale plus exigeante : la fusée démarre **à la fois inclinée ET décalée latéralement**.

    $$
    s(0) = (x_0,\ 0,\ 10,\ -2,\ \theta_0,\ 0), \quad x_0 = 2.5\ \text{m}, \quad \theta_0 = \pi/6.
    $$

    Le retour d'état $\phi = -K\,(x, \dot x, \theta, \omega)^\top$ pénalise les 4 états et les ramène simultanément vers zéro. À l'arrivée :

    - la fusée est **recentrée** au-dessus du pad ($x(T)$ très proche de 0),
    - elle est **verticale** ($\theta(T)$ proche de 0),
    - la vitesse verticale est nulle ($\dot y(T) = 0$).

    Le déplacement latéral $x$ est plus dur à amener à 0 que $\theta$ : la commande disponible $\phi$ agit *directement* sur le couple (rotation) mais *indirectement* sur $x$ — via $\theta$ qui pousse latéralement. Avec $T=5$ s on a juste assez de temps pour converger.
    """)
    return


@app.cell
def _(animate_scenario, mo, np, tilted_landing_law):
    THETA_0_OFFSET = np.pi / 6
    X_0 = 2.5
    mo.md(
        rf"### 6. Off-center tilted landing ($x_0 = 2.5$ m, $\theta_0 = 30^\circ$)"
    )
    mo.Html(
        animate_scenario(
            [X_0, 0.0, 10.0, -2.0, THETA_0_OFFSET, 0.0],
            tilted_landing_law(THETA_0_OFFSET),
        )
    ).center()
    return


if __name__ == "__main__":
    app.run()
