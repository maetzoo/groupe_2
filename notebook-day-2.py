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

    return np, plt, scipy


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

    Define the Python constants `g`, `M` and `l` that correspond to the gravity constant, the mass and length of the booster.
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md("""
    ### 🔓 Solution
    """)
    return


@app.cell(hide_code=True)
def _():
    g = 1.0
    M = 1.0
    l = 2
    return M, g, l


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ## 🧩 Forces

    Compute the cartesian coordinates $f_x$ and $f_y$ of the force applied to the booster by the reactor, as functions of $f$, $\theta$ and $\phi$.
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md("""
    ### 🔓 Solution
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    Given the geometric setting, the cartesian coordinates of the unit vector $\vec{u}=(u_x, u_y)$ aligned with the reactor (or flame) axis and pointing from the reactor towards the flame satisfy:

    \begin{align*}
    u_x & = +\sin (\theta + \phi) \\
    u_y & = -\cos(\theta +\phi)
    \end{align*}

    Assuming that $f \geq 0$, the force applied to the booster is in the opposite direction and has amplitude $f$:

    $$
    \vec{f} = -f \vec{u}
    $$

    Therefore,

    \begin{align*}
    f_x & = -f \sin (\theta + \phi) \\
    f_y & = +f \cos(\theta +\phi)
    \end{align*}
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ## 🧩 Center of Mass

    Give the ordinary differential equation that governs the evolution of the position $(x, y)$ of the center of mass of the booster.
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md("""
    ### 🔓 Solution
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    The force exerted by the gravity on the booster is

    $$
    \vec{f}_g =
    \begin{bmatrix}
    0 \\ - M g
    \end{bmatrix}
    $$

    By Newton's second law of motion, the acceleration $\vec{a} = (\ddot{x}, \ddot{y})$
    satisfies $M \vec{a} = \vec{f} + \vec{f}_g$ and thus

    \begin{align*}
    M \ddot{x} & = -f \sin (\theta + \phi) \\
    M \ddot{y} & = +f \cos(\theta +\phi) - Mg
    \end{align*}
    """)
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
    ### 🔓 Solution

    The moment of inertia of a thin rod with uniformly distributed mass about its center is of mass is

    $$
    J = \frac{1}{12} M \ell^2
    $$
    """)
    return


@app.cell
def _(M, l):
    J = M * l ** 2 / 12
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
    ### 🔓 Solution

    Newton's Second Law for Rotation is $J \ddot{\theta} = \tau$ where $\tau$ is the torque applied to the booster. Here the torque applied by the gravity to the booster is $0$ by symmetry and only the booster reactor induces a torque. The torque can be
    first computed as a vector in 3D as the cross-product of the vector between the center of the booster and the reactor location and the force applied by the reactor.
    Afterwards, we can be project it on the 3rd axis to get $\tau$.

    Thus, we have

    $$
    \tau =
    \left(
    \ell / 2
    \begin{bmatrix}
    {} +\sin \theta \\ - \cos \theta \\ 0
    \end{bmatrix}
    \wedge \begin{bmatrix} -f \sin (\theta + \phi) \\ +f \cos (\theta + \phi) \\ 0
    \end{bmatrix}
    \right)
    \cdot \begin{bmatrix} 0 \\ 0 \\ 1 \end{bmatrix}
    =
    \ell/2 (f\sin \theta \cos (\theta + \phi) - f\sin (\theta + \phi) \cos \theta).
    $$

    Since $\sin \alpha \cos \beta - \sin \beta \cos \alpha = \sin (\alpha - \beta)$,
    we obtain

    $$
    \tau = - f (\ell/2) \sin \phi,
    $$

    thus the angular acceleration is governed by

    $$
    J \ddot{\theta} = - f (\ell / 2)  \sin \phi.
    $$
    """)
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
    ### 🔓 Solution

    Given that

    \begin{align*}
    M \ddot{x} & = -f \sin (\theta + \phi) \\
    M \ddot{y} & = +f \cos(\theta +\phi) - Mg \\
    J \ddot{\theta} & = - f (\ell/2) \sin \phi
    \end{align*}

    and $\dot{x} = v_x$, $\dot{y} = v_y$ and $\dot{\theta} = \omega$, we
    can use as a state vector $s = (x, v_x, y, v_y, \theta, \omega) \in \mathbb{R}^6$
    and the corresponding function $F$ is given by

    $$
    F(s, f, \phi) = \begin{bmatrix}
    v_x \\ -(f / M) \sin (\theta + \phi) \\
    v_y \\ +(f / M) \cos(\theta +\phi) - g \\
    \omega \\ - (f / J) (\ell/2) \sin \phi
    \end{bmatrix}
    $$
    """)
    return


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


@app.cell(hide_code=True)
def _(mo):
    mo.md("""
    ### 🔓 Solution
    """)
    return


@app.cell(hide_code=True)
def _(J, M, g, l, np, scipy):
    def redstart_solve(t_span, y0, f_phi):
        def fun(t, state):
            x, vx, y, vy, theta, omega = state
            f, phi = f_phi(t, state)
            d2x = (-f * np.sin(theta + phi)) / M
            d2y = (+ f * np.cos(theta + phi)) / M - g
            d2theta = - (f / J) * (l / 2) * np.sin(phi)
            return np.array([vx, d2x, vy, d2y, omega, d2theta])
        r = scipy.integrate.solve_ivp(fun, t_span, y0, dense_output=True)
        return r.sol

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
    ### 🔓 Solution

    In the free fall scenario, the solution satisfies $x(t)=0$, $y(t) = y(0) - g/2 t^2$ and $\theta(t) = 0$. Since numerically $y(0)=10.0$, $g=1$ and $\ell=2$, the threshold
    is crossed when $10 - 1/2 t^2 = 2$, that is $t=4$.
    """)
    return


@app.cell(hide_code=True)
def _(l, np, plt, redstart_solve):
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
    mo.md("""
    ### 🔓 Solution
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    We can search for a cubic polynomial

    $$
    y(t) = a_3 t^3 + a_2 t^2 + a_1 t + a_0
    $$

    that solves the four given constraints,
    then deduce $f(t)$ from the equation $M \ddot{y} = f + Mg$.

    The time derivative of $y$ satisfies
    $$
    \dot{y}(t) = 3 a_3 t^2 + 2 a_2 t + a_1,
    $$
    thus the constraints are:

    \begin{align*}
    y(0) = a_0 &= 10, \\
    \dot{y}(0) = a_1 &= -2,\\
    y(5) = 125 a_3 + 25 a_2 + 5 a_1 + a_0 &= 1, \\
    \dot{y}(5) = 75 a_3 + 10 a_2 + a_1 &= 0. \\
    \end{align*}

    The solution of this linear system provides:

    $$
    y(t)
    =\frac{8}{125}t^3 - \frac{7}{25} t^2 - 2t + 10,
    $$
    which yields
    $$
    \ddot{y}(t)
    =
    \frac{48}{125}t - \frac{14}{25}
    $$
    and therefore since $M=1$ and $g=1$,
    $$
    f(t) = \frac{\ddot{y}(t)}{M} + g = \frac{48}{125}t + \frac{11}{25}.
    $$
    """)
    return


@app.cell(hide_code=True)
def _(l, np, plt, redstart_solve):
    def controlled_landing_example():
        t_span = [0.0, 5.0]
        y0 = [0.0, 0.0, 10.0, -2.0, 0.0, 0.0]
        def f_phi_smooth_landing(t, state):
            return np.array([48 / 125 * t + 11 / 25, 0])
        sol = redstart_solve(t_span, y0, f_phi=f_phi_smooth_landing)
        t = np.linspace(t_span[0], t_span[1], 1000)
        y_t = sol(t)[2]
        plt.plot(t, y_t, label=r"$y(t)$ (height in meters)")
        plt.plot(t, (l / 2) * np.ones_like(t), color="grey", ls="--", label=r"$y=\ell/2$")
        plt.title("Controlled Landing")
        plt.xlabel("time $t$")
        plt.grid(True)
        plt.legend()
        return plt.gcf()
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


@app.cell(hide_code=True)
def _(mo):
    mo.md("""
    ### 🔓 Solution
    """)
    return


@app.cell
def _(svg, transform):
    def world(view_box, *objects):
        x_min, x_max, y_min, y_max = view_box    
        width, height = x_max - x_min, y_max - y_min

        return svg.svg(
          xmlns="http://www.w3.org/2000/svg",
          viewBox=f"0 0 {width} {height}",
          style="max-height:80vh")(
              transform.translate(x=-x_min, y=y_max)(
                  transform.scale(y=-1.0)(
                      # Sky
                      svg.rect(x=-1e3, y=0, width=2e3, height=1e3, fill="lightskyblue"),
                      # Ground
                      svg.rect(x=-1e3, y=-2e3, width=2e3, height=2e3, fill="sandybrown"),
                      # Target 
                      svg.rect(x=-1, y =-1, width=2, height=1, fill="lightgreen"),
                      *objects,
                )
            )
        )

    return (world,)


@app.cell
def _(mo, svg, world):
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


@app.cell(hide_code=True)
def _(mo):
    mo.md("""
    ### 🔓 Solution
    """)
    return


@app.cell
def _(M, g, l, np, svg, transform):
    def booster(x, y, theta, f, phi):
        flame_length = (l / 2) * (f / M / g)
        return transform.translate(x, y)(
            transform.rotate(theta / np.pi * 180.0)(
                svg.rect(x=-l/20, y=-l/2, width=l/10, height=l, fill="black"),
                transform.translate(0, -l / 2)(
                    transform.rotate(phi / np.pi * 180)(
                        svg.rect(
                            x=-l/20,
                            y=-flame_length,
                            width=l/10,
                            height=flame_length,
                            fill="red",
                        )
                    )
                )
            )
        )

    return (booster,)


@app.cell(hide_code=True)
def _(M, booster, g, l, mo, np, world):
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


@app.cell(hide_code=True)
def _(mo):
    mo.md("""
    ### 🔓 Solution
    """)
    return


@app.cell
def _(M, animate_transform, g, l, np, svg):
    def booster_anim(x, y, theta, f, phi, T):
        if not callable(theta):
            theta_cst = theta
            theta = lambda t: theta_cst
        if not callable(phi):
            phi_cst = phi
            phi = lambda t: phi_cst

        def theta_deg(t):
            return theta(t) / np.pi * 180.0

        def phi_deg(t):
            return phi(t) / np.pi * 180.0

        return animate_transform.translate(x, y, T=T)(
            animate_transform.rotate(theta_deg, T=T)(
                svg.rect(
                    x=-l / 20,
                    y=-l/2,
                    width=l / 10,
                    height=l,
                    fill="black",
                ),
                animate_transform.translate(y=-l/2, T=T)(
                    animate_transform.rotate(phi_deg, T=T)(
                        animate_transform.scale(y=f, T=T)(
                            svg.rect(
                                x=-l/20,
                                y=-1/M/g,
                                width=l / 10,
                                height=1/M/g,
                                fill="red",
                            )
                        )
                    )
                ),
            )
        )

    return (booster_anim,)


@app.cell
def _(M, booster_anim, g, l, np):
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

    return (booster_anim_0,)


@app.cell
def _(booster_anim_0, mo, world):
    mo.Html(
        world([-3, 3, -2, 4], booster_anim_0())
    ).center() 
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


@app.cell(hide_code=True)
def _(mo):
    mo.md("""
    ### 🔓 Solution
    """)
    return


@app.cell
def _(booster_anim, mo, np, redstart_solve, world):
    def anim_1():
        t_span = [0.0, 5.0]
        y0 = [0.0, 0.0, 10.0, 0.0, 0.0, 0.0] 
        def f_phi(t, state):
            return np.array([0, 0])
        sol = redstart_solve(t_span, y0, f_phi)
        x = lambda t: sol(t)[0]
        y = lambda t: sol(t)[2]
        theta = lambda t : sol(t)[4]
        f = lambda t: f_phi(t, sol(t))[0]
        phi = lambda t: f_phi(t, sol(t))[0]
        return mo.Html(
            world(
                [-3, 3, -2, 12], 
                booster_anim(x, y, theta, f, phi, T=t_span[1])
            )
        ).center()

    anim_1()
    return


@app.cell
def _(M, booster_anim, g, mo, np, redstart_solve, world):
    def anim_2():
        t_span = [0.0, 5.0]
        y0 = [0.0, 0.0, 10.0, 0.0, 0.0, 0.0]
        def f_phi(t, state):
            return np.array([M * g, 0])
        sol = redstart_solve(t_span, y0, f_phi)
        x = lambda t: sol(t)[0]
        y = lambda t: sol(t)[2]
        theta = lambda t : sol(t)[4]
        f = lambda t: f_phi(t, sol(t))[0]
        phi = lambda t: f_phi(t, sol(t))[1]
        return mo.Html(
            world(
                [-3, 3, -2, 12], 
                booster_anim(x, y, theta, f, phi, T=t_span[1])
            )
        ).center()

    anim_2()
    return


@app.cell
def _(M, booster_anim, g, mo, np, redstart_solve, world):
    def anim_3():
        t_span = [0.0, 5.0]
        y0 = [0.0, 0.0, 10.0, 0.0, 0.0, 0.0]
        def f_phi(t, state):
            return np.array([M * g, np.pi / 8])
        sol = redstart_solve(t_span, y0, f_phi)
        x = lambda t: sol(t)[0]
        y = lambda t: sol(t)[2]
        theta = lambda t : sol(t)[4]
        f = lambda t: f_phi(t, sol(t))[0]
        phi = lambda t: f_phi(t, sol(t))[1]
        return mo.Html(
            world(
                [-3, 3, -2, 12], 
                booster_anim(x, y, theta, f, phi, T=t_span[1])
            )
        ).center()

    anim_3()
    return


@app.cell
def _(booster_anim, mo, np, redstart_solve, world):
    def anim_4():
        t_span = [0.0, 5.0]
        y0 = [0.0, 0.0, 10.0, -2.0, 0.0, 0.0]
        def f_phi(t, state):
            return np.array([48 / 125 * t + 11 / 25, 0])
        sol = redstart_solve(t_span, y0, f_phi)
        x = lambda t: sol(t)[0]
        y = lambda t: sol(t)[2]
        theta = lambda t : sol(t)[4]
        f = lambda t: f_phi(t, sol(t))[0]
        phi = lambda t: f_phi(t, sol(t))[1]
        return mo.Html(
            world(
                [-3, 3, -2, 12], 
                booster_anim(x, y, theta, f, phi, T=t_span[1])
            )
        ).center()

    anim_4()
    return


@app.cell
def _(mo):
    mo.md(r"""
    # Linearized Dynamics
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ## 🧩 Equilibria

    We assume that

    - $|\theta| < \pi/2$,
    - $|\phi| < \pi/2$, and
    - $f > 0$.

    What are the possible equilibria of the system for constant inputs $f$ and $\phi$ and what are the corresponding values of these inputs?
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ###

    Pour trouver les points d'équilibre, on cherche les états où le système ne bouge plus : les dérivées temporelles sont nulles ($\dot{x}=\dot{y}=\dot{\theta}=0$ et $\ddot{x}=\ddot{y}=\ddot{\theta}=0$).

    D'après nos équations de la dynamique :
    1. $J\ddot{\theta} = -f(\ell/2)\sin(\phi) = 0$. Puisque $f > 0$, cela implique $\sin(\phi) = 0$. Comme $|\phi| < \pi/2$, on a **$\phi = 0$**.
    2. $M\ddot{x} = -f\sin(\theta + \phi) = 0$. Sachant que $\phi = 0$ et $f > 0$, on a $\sin(\theta) = 0$. Puisque $|\theta| < \pi/2$, on a **$\theta = 0$**.
    3. $M\ddot{y} = f\cos(\theta + \phi) - Mg = 0$. En remplaçant $\theta = 0$ et $\phi = 0$, on obtient $f\cos(0) = Mg$, d'où **$f = Mg$**.

    **Conclusion :** Les équilibres possibles correspondent au **vol stationnaire parfait (hover)**. La fusée est immobile ($v_x=v_y=\omega=0$), parfaitement verticale ($\theta = 0$), avec la tuyère alignée ($\phi = 0$) et une poussée qui compense exactement la gravité ($f = Mg$).
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ## 🧩 Linearized Model

    Introduce the error variables $\Delta x$, $\Delta y$, $\Delta \theta$, and $\Delta f$ and $\Delta \phi$ of the state and input values with respect to the generic equilibrium configuration.
    What are the linear ordinary differential equations that govern (approximately) these variables in a neighbourhood of the equilibrium?
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ###

    On introduit les variables d'erreur autour de l'équilibre de vol stationnaire ($f_e = Mg$, $\theta_e = 0$, $\phi_e = 0$) :
    * État : $x = x_e + \Delta x$, $y = y_e + \Delta y$, $\theta = 0 + \Delta \theta$
    * Entrées : $f = Mg + \Delta f$, $\phi = 0 + \Delta \phi$

    Pour de petits angles, on utilise les approximations $\sin(\alpha) \approx \alpha$ et $\cos(\alpha) \approx 1$. Les équations linéarisées deviennent :

    **Axe $x$ :** $\ddot{\Delta x} = -\frac{Mg + \Delta f}{M}\sin(\Delta \theta + \Delta \phi) \approx -\frac{Mg + \Delta f}{M}(\Delta \theta + \Delta \phi)$
    En négligeant le terme du second ordre $\Delta f(\Delta \theta + \Delta \phi)$, on obtient :
    $$\ddot{\Delta x} = -g(\Delta \theta + \Delta \phi)$$

    **Axe $y$ :**
    $\ddot{\Delta y} = \frac{Mg + \Delta f}{M}\cos(\Delta \theta + \Delta \phi) - g \approx \frac{Mg + \Delta f}{M}(1) - g$
    $$\ddot{\Delta y} = \frac{\Delta f}{M}$$

    **Angle $\theta$ :**
    $\ddot{\Delta \theta} = -\frac{(Mg + \Delta f)\ell}{2J}\sin(\Delta \phi) \approx -\frac{(Mg + \Delta f)\ell}{2J}\Delta \phi$
    En négligeant le terme du second ordre $\Delta f \Delta \phi$, on obtient :
    $$\ddot{\Delta \theta} = -\frac{Mg\ell}{2J}\Delta \phi$$
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ## 🧩 Standard Form

    1. What are the matrices $A$ and $B$ associated to this linear model in standard form?
    2. Define the corresponding NumPy arrays `A` and `B`.
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ###

    Le vecteur d'état est $\Delta s = [\Delta x, \Delta v_x, \Delta y, \Delta v_y, \Delta \theta, \Delta \omega]^T$ et le vecteur d'entrée est $\Delta u = [\Delta f, \Delta \phi]^T$.

    L'équation d'état sous la forme $\dot{\Delta s} = A \Delta s + B \Delta u$ s'écrit avec les matrices suivantes :

    $$
    A =
    \begin{bmatrix}
    0 & 1 & 0 & 0 & 0 & 0 \\
    0 & 0 & 0 & 0 & -g & 0 \\
    0 & 0 & 0 & 1 & 0 & 0 \\
    0 & 0 & 0 & 0 & 0 & 0 \\
    0 & 0 & 0 & 0 & 0 & 1 \\
    0 & 0 & 0 & 0 & 0 & 0
    \end{bmatrix}
    , \quad
    B =
    \begin{bmatrix}
    0 & 0 \\
    0 & -g \\
    0 & 0 \\
    1/M & 0 \\
    0 & 0 \\
    0 & -\frac{Mg\ell}{2J}
    \end{bmatrix}
    $$
    """)
    return


@app.cell
def _(J, M, g, l, np):
    # Cellule pour définir les matrices A et B du modèle linéarisé
    A = np.array([
        [0.0, 1.0, 0.0, 0.0,  0.0, 0.0],
        [0.0, 0.0, 0.0, 0.0,   -g, 0.0],
        [0.0, 0.0, 0.0, 1.0,  0.0, 0.0],
        [0.0, 0.0, 0.0, 0.0,  0.0, 0.0],
        [0.0, 0.0, 0.0, 0.0,  0.0, 1.0],
        [0.0, 0.0, 0.0, 0.0,  0.0, 0.0]
    ])

    B = np.array([
        [0.0,   0.0],
        [0.0,   -g],
        [0.0,   0.0],
        [1.0/M, 0.0],
        [0.0,   0.0],
        [0.0,   -(M * g * l) / (2 * J)]
    ])

    A, B
    return A, B


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ## 🧩 Stability

    Is the generic equilibrium asymptotically stable?
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ###

    Pour déterminer si l'équilibre générique est asymptotiquement stable, nous devons analyser les valeurs propres (eigenvalues) de la matrice de dynamique $A$.

    D'après le cours, un système linéaire est asymptotiquement stable si et seulement si toutes les valeurs propres de sa matrice ont une partie réelle strictement négative (dans le demi-plan gauche ouvert).

    Notre matrice $A$ est une matrice dont le polynôme caractéristique donne uniquement des racines nulles (c'est une matrice nilpotente). Ses 6 valeurs propres sont donc toutes égales à $0$.

    **Conclusion :** Puisque les parties réelles des valeurs propres ne sont pas strictement négatives, l'équilibre générique **n'est pas asymptotiquement stable**.
    """)
    return


@app.cell
def _(A, np):

    valeurs_propres = np.linalg.eigvals(A)

    print("Valeurs propres de la matrice A :")
    print(np.round(valeurs_propres, 3))

    est_stable = np.all(np.real(valeurs_propres) < 0)
    print(f"Le système est-il asymptotiquement stable ? {est_stable}")
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ## 🧩 Controllability

    Is the linearized model controllable?
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ###

    Pour savoir si le modèle linéarisé est commandable (controllable), nous utilisons le critère de Kalman.
    Un système invariant dans le temps de dimension $n$ est totalement commandable si la matrice de commandabilité $\mathcal{C}$ est de rang plein (c'est-à-dire de rang $n$).

    La matrice de commandabilité est construite en concaténant les matrices suivantes :
    $$\mathcal{C} = \begin{bmatrix} B & AB & A^2B & A^3B & A^4B & A^5B \end{bmatrix}$$

    Ici, la dimension de notre vecteur d'état est $n = 6$. Si le rang de la matrice $\mathcal{C}$ (qui est de taille $6 \times 12$) est égal à 6, alors le système est commandable.

    Physiquement, cela a du sens :
    - L'entrée $\Delta f$ contrôle directement l'altitude $y$.
    - L'entrée $\Delta \phi$ contrôle l'angle de la fusée $\theta$, et l'inclinaison de cet angle $\theta$ permet à son tour de contrôler le déplacement latéral $x$.
    Toutes les variables d'état peuvent donc être pilotées !
    """)
    return


@app.cell
def _(A, B, np):

    def KCM(A, B):
        n = np.shape(A)[0]
        mp = np.linalg.matrix_power
        cs = np.column_stack
        return cs([mp(A, k) @ B for k in range(n)])


    n = A.shape[0]


    C_matrix = KCM(A, B)


    rang_C = np.linalg.matrix_rank(C_matrix)

    print(f"Dimension du système (n) : {n}")
    print(f"Rang de la matrice de commandabilité C : {rang_C}")
    print(f"Le système est-il commandable ? {rang_C == n}")
    print(C_matrix)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ## 🧩 Lateral Dynamics

    We limit our interest in the lateral position $x$, the tilt $\theta$ and their derivatives (we are for the moment fine with letting $y$ and $\dot{y}$ be uncontrolled). We also set $f = M g$ and control the system only with $\phi$.

    - What are the new (reduced) matrices $A$ and $B$ for this reduced system?

    - Check the controllability of this new system.
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ###

    **1. Matrices du système réduit**
    Nous conservons uniquement les états liés à la dynamique latérale : $\Delta s_{lat} = [\Delta x, \Delta v_x, \Delta \theta, \Delta \omega]^T$.
    La poussée étant fixée à $f = Mg$, la variation d'entrée est nulle ($\Delta f = 0$). Notre seule commande est l'angle de la tuyère $\Delta u = \Delta \phi$.

    En extrayant les lignes et colonnes correspondantes des matrices pleines définies précédemment, nous obtenons le système réduit $\dot{\Delta s}_{lat} = A_{lat} \Delta s_{lat} + B_{lat} \Delta \phi$ avec :

    $$
    A_{lat} =
    \begin{bmatrix}
    0 & 1 & 0 & 0 \\
    0 & 0 & -g & 0 \\
    0 & 0 & 0 & 1 \\
    0 & 0 & 0 & 0
    \end{bmatrix}
    , \quad
    B_{lat} =
    \begin{bmatrix}
    0 \\
    -g \\
    0 \\
    -\frac{Mg\ell}{2J}
    \end{bmatrix}
    $$

    **2. Commandabilité**
    D'après le cours, un système linéaire invariant dans le temps de dimension $n$ est commandable si et seulement si sa matrice de commandabilité $\mathcal{C} = [B, AB, \dots, A^{n-1}B]$ est de rang plein (égal à $n$).

    Ici, $n=4$. Calculons les colonnes de la matrice de Kalman :
    * $B_{lat} = [0, -g, 0, -\beta]^T$ (en posant $\beta = \frac{Mg\ell}{2J}$)
    * $A_{lat}B_{lat} = [-g, 0, -\beta, 0]^T$
    * $A_{lat}^2B_{lat} = [0, g\beta, 0, 0]^T$
    * $A_{lat}^3B_{lat} = [g\beta, 0, 0, 0]^T$

    La matrice $\mathcal{C}$ est triangulaire (à des permutations de lignes et colonnes près) avec des éléments non nuls sur la diagonale principale. Son déterminant est non nul, elle est donc de rang 4. **Le système réduit est totalement commandable**.
    """)
    return


@app.cell
def _(J, M, g, l, np):

    A_lat = np.array([
        [0.0, 1.0, 0.0, 0.0],
        [0.0, 0.0,  -g, 0.0],
        [0.0, 0.0, 0.0, 1.0],
        [0.0, 0.0, 0.0, 0.0]
    ])

    beta = (M * g * l) / (2 * J)
    B_lat = np.array([
        [0.0],
        [-g],
        [0.0],
        [-beta]
    ])

    # vérification de la commandabilité (Critère de Kalman)
    n_lat = A_lat.shape[0]
    C_lat_cols = [B_lat]
    terme_actuel = B_lat
    for _ in range(1, n_lat):
        terme_actuel = A_lat @ terme_actuel
        C_lat_cols.append(terme_actuel)

    C_lat = np.hstack(C_lat_cols)
    rang_C_lat = np.linalg.matrix_rank(C_lat)

    print(f"Rang de la matrice de commandabilité réduite : {rang_C_lat} (n={n_lat})")
    print(f"Le système latéral est-il commandable ? {rang_C_lat == n_lat}")
    return A_lat, B_lat


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ## 🧩 Linear Model in Free Fall

    Make graphs of $x(t)$ and $\theta(t)$ for the linearized model when
    - $x(0)=0$, $\dot{x}(0)=0$, $\theta(0) = \pi/4$, $\dot{\theta}(0) =0$, and
    - $\phi(t)=0$ at all times.

    What do you see? How do you explain it?
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    Nous simulons le modèle linéarisé autonome ($\Delta \phi = 0$) avec une condition initiale inclinée $\Delta s_{lat}(0) = [0, 0, \pi/4, 0]^T$.

    **Observation :**
    Sur le graphique généré, nous pouvons voir que l'angle $\theta(t)$ reste constant à sa valeur initiale de $\pi/4$ (soit environ 0.785 rad). La position latérale $x(t)$, quant à elle, dérive de manière parabolique vers les valeurs négatives.

    **Explication :**
    Ce comportement s'explique directement par la structure de notre matrice $A_{lat}$.
    * La dernière ligne de $A_{lat}$ est composée uniquement de zéros, ce qui signifie que l'accélération angulaire $\ddot{\theta}$ est strictement nulle en l'absence de commande d'entrée ($\Delta \phi = 0$). L'angle initial est donc conservé indéfiniment.
    * La deuxième ligne de $A_{lat}$ donne l'accélération horizontale : $\ddot{x} = -g \theta$. Puisque $\theta$ est constant et positif ($\pi/4$), la fusée subit une accélération constante vers la gauche. En intégrant deux fois cette accélération constante, on obtient naturellement une trajectoire en forme de parabole pour la position $x(t) = -\frac{g \pi}{8} t^2$.
    """)
    return


@app.cell
def _(A_lat, np, plt):

    from scipy.linalg import expm

    def simulate_linear_free_fall():
        t = np.linspace(0.0, 5.0, 500)
        y0_lat = np.array([0.0, 0.0, np.pi/4, 0.0])
    
   
        yt = np.array([expm(A_lat * t_) @ y0_lat for t_ in t])
    
        x_t = yt[:, 0]
        theta_t = yt[:, 2]
    
        fig, axes = plt.subplots(2, 1, figsize=(8, 6), sharex=True)
    
        axes[0].plot(t, x_t, label=r"Position latérale $x(t)$", color="tab:blue")
        axes[0].set_ylabel("x (m)")
        axes[0].grid(True)
        axes[0].legend()
    
        axes[1].plot(t, theta_t, label=r"Angle d'inclinaison $\theta(t)$", color="tab:red")
        axes[1].set_ylabel(r"$\theta$ (rad)")
        axes[1].set_xlabel("Temps $t$ (s)")
        axes[1].grid(True)
        axes[1].legend()
    
        fig.suptitle("Simulation du modèle latéral linéarisé (Sans commande, $\phi=0$)")
        fig.tight_layout()
        return fig

    simulate_linear_free_fall()
    return (expm,)


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ## 🧩 Manually Tuned Controller

    Try to find the two missing coefficients of the matrix

    $$
    K =
    \begin{bmatrix}
    0 & 0 & ? & ?
    \end{bmatrix}
    \in \mathbb{R}^{4\times 1}
    $$

    such that the control law

    $$
    \Delta \phi(t) = - K \cdot
    \begin{bmatrix}
    \Delta x(t) \\
    \Delta \dot{x}(t) \\
    \Delta \theta(t) \\
    \Delta \dot{\theta}(t)
    \end{bmatrix} \in \mathbb{R}
    $$

    manages  when
    $\Delta x(0)=0$, $\Delta \dot{x}(0)=0$, $\Delta \theta(0) = 45 / 180  \times \pi$  and $\Delta \dot{\theta}(0) =0$ to:

    - make $\Delta \theta(t) \to 0$ in approximately $20$ sec (or less),
    - $|\Delta \theta(t)| < \pi/2$ and $|\Delta \phi(t)| < \pi/2$ at all times,
    - (but we don't care about a possible drift of $\Delta x(t)$).

    Explain your thought process, show your iterative guesses and simulations!

    Is your final closed-loop model asymptotically stable?
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ###

    **1. Réflexion et choix des gains $k_3$ et $k_4$**
    Nous cherchons une matrice $K = [0, 0, k_3, k_4]$. La loi de commande est $\Delta \phi = -k_3 \Delta \theta - k_4 \Delta \omega$.
    Puisque les deux premiers gains sont nuls, la dynamique de l'angle $\theta$ est complètement découplée de la position $x$. D'après nos équations linéarisées :
    $$\ddot{\Delta \theta} = -\frac{Mg\ell}{2J} \Delta \phi = \frac{Mg\ell}{2J} (k_3 \Delta \theta + k_4 \Delta \omega)$$

    En posant $\alpha = \frac{Mg\ell}{2J}$ (qui vaut $1.5$ avec nos constantes $M=1, g=1, l=1, J=1/3$), l'équation caractéristique du sous-système angulaire est :
    $$s^2 - \alpha k_4 s - \alpha k_3 = 0$$

    Pour que l'angle $\Delta \theta$ converge vers $0$ en environ 20 secondes, nous avons besoin d'une constante de temps $\tau \approx 4$ à $5$ secondes, ce qui correspond à des pôles autour de $-0.2$ ou $-0.25$.
    Si l'on vise par exemple un polynôme $(s+0.2)(s+0.3) = s^2 + 0.5s + 0.06$, on identifie :
    * $-\alpha k_4 = 0.5 \implies k_4 = -0.5 / 1.5 \approx -0.33$
    * $-\alpha k_3 = 0.06 \implies k_3 = -0.06 / 1.5 = -0.04$

    Avec $K = [0, 0, -0.04, -0.33]$, l'effort de commande initial sera $\Delta \phi(0) = -(-0.04)(\pi/4) \approx 0.03$ rad, ce qui respecte largement la contrainte $|\Delta \phi| < \pi/2$.

    **2. Stabilité asymptotique du modèle en boucle fermée**
    Le modèle complet **n'est pas asymptotiquement stable**.
    Bien que nous ayons stabilisé le sous-système angulaire ($\Delta \theta \to 0$ et $\Delta \omega \to 0$), la matrice en boucle fermée $A_{cl} = A - B_{lat}K$ possède toujours deux valeurs propres égales à zéro correspondant aux états non contrôlés $\Delta x$ et $\Delta v_x$. D'après le cours, un système n'est asymptotiquement stable que si *toutes* ses valeurs propres ont une partie réelle strictement négative. La simulation montrera que la position latérale $x(t)$ dérive sans jamais revenir à 0.
    """)
    return


@app.cell
def _(A_lat, B_lat, np, plt):
    def _():
        from scipy.linalg import expm

        def simulate_manual_controller():
        
            k3, k4 = -0.04, -0.33
            K_man = np.array([[0.0, 0.0, k3, k4]])
        
       
            A_cl_man = A_lat - B_lat @ K_man
        
       
            eig_man = np.linalg.eigvals(A_cl_man)
            print("Valeurs propres avec K manuel :", np.round(eig_man, 3))
        
       
            t = np.linspace(0.0, 20.0, 1000)
            y0_lat = np.array([0.0, 0.0, np.pi/4, 0.0]) 
        
        
            yt = np.array([expm(A_cl_man * t_) @ y0_lat for t_ in t])
        
            theta_t = yt[:, 2]
            x_t = yt[:, 0]
        
            phi_t = np.array([-K_man @ state for state in yt]).flatten()
        
       
            fig, axes = plt.subplots(3, 1, figsize=(8, 8), sharex=True)
        
            axes[0].plot(t, theta_t, color="tab:red", label=r"$\Delta \theta(t)$ (rad)")
            axes[0].axhline(0, color="grey", ls="--")
            axes[0].set_ylabel("Angle")
            axes[0].legend()
            axes[0].grid(True)
        
            axes[1].plot(t, phi_t, color="tab:green", label=r"$\Delta \phi(t)$ (rad)")
            axes[1].axhline(0, color="grey", ls="--")
            axes[1].set_ylabel("Commande")
            axes[1].legend()
            axes[1].grid(True)
        
            axes[2].plot(t, x_t, color="tab:blue", label=r"$\Delta x(t)$ (m) - DÉRIVE")
            axes[2].set_xlabel("Temps $t$ (s)")
            axes[2].set_ylabel("Position")
            axes[2].legend()
            axes[2].grid(True)
        
            fig.suptitle("Manually Tuned Controller (Dérive de la position)")
            fig.tight_layout()
            return fig
        return simulate_manual_controller()


    _()
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ## 🧩 Controller Tuned with Pole Assignment

    Using pole assignement, find a matrix

    $$
    K_{pp} =
    \begin{bmatrix}
    ? & ? & ? & ?
    \end{bmatrix}
    \in \mathbb{R}^{4\times 1}
    $$

    such that the control law

    $$
    \Delta \phi(t)
    = - K_{pp} \cdot
    \begin{bmatrix}
    \Delta x(t) \\
    \Delta \dot{x}(t) \\
    \Delta \theta(t) \\
    \Delta \dot{\theta}(t)
    \end{bmatrix} \in \mathbb{R}
    $$

    satisfies the conditions defined for the manually tuned controller and additionally:

    - result in an asymptotically stable closed-loop dynamics,

    - make $\Delta x(t) \to 0$ in approximately $20$ sec (or less).

    Explain how you find the proper design parameters!
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ###

    **Méthode de conception et choix des pôles**
    Pour que le système complet soit **asymptotiquement stable**, nous devons placer l'ensemble des 4 pôles du système dans le demi-plan complexe gauche. De plus, nous voulons un temps de réponse d'environ 20 secondes, ce qui nécessite des pôles (valeurs propres dominantes) autour de $-0.2$ à $-0.3$.

    *Contrainte de la fonction `place_poles` :* Le cours précise que la fonction `scipy.signal.place_poles` refuse d'assigner des valeurs propres dont la multiplicité est supérieure au rang de la matrice $B$. Puisque notre matrice $B_{lat}$ est de rang 1 (une seule colonne), nous **devons impérativement choisir 4 pôles distincts**.

    Nous choisissons les pôles : `[-0.2, -0.22, -0.24, -0.26]`.
    Ces pôles sont suffisamment proches de zéro pour éviter que le système ne réagisse trop violemment au début (ce qui violerait la condition de saturation $|\Delta \phi| < \pi/2$), mais suffisamment éloignés pour garantir que $\Delta x$ et $\Delta \theta$ retournent à $0$ en moins de 20 secondes.

    Contrairement au cas manuel, la matrice $K_{pp}$ calculée par l'algorithme n'aura pas de zéros : elle prendra en compte la position $\Delta x$ et la vitesse $\Delta v_x$, forçant ainsi la fusée à s'incliner légèrement dans le sens opposé pour freiner sa dérive latérale et revenir parfaitement à sa position d'origine.
    """)
    return


@app.cell
def _(A_lat, B_lat, expm, np, plt):
    import scipy.signal as sig

    def simulate_pole_placement_controller():
    
        poles = [-0.20, -0.22, -0.24, -0.26]
    
    
        K_pp = sig.place_poles(A_lat, B_lat, poles).gain_matrix
    
        A_cl_pp = A_lat - B_lat @ K_pp
    
        eig_pp = np.linalg.eigvals(A_cl_pp)
        print("Matrice de gain K_pp :", np.round(K_pp, 3))
        print("Valeurs propres avec K_pp :", np.round(eig_pp, 3))
    
        # Simulation
        t = np.linspace(0.0, 25.0, 1000)
        y0_lat = np.array([0.0, 0.0, np.pi/4, 0.0])
    
        yt = np.array([expm(A_cl_pp * t_) @ y0_lat for t_ in t])
    
        x_t = yt[:, 0]
        theta_t = yt[:, 2]
        phi_t = np.array([-K_pp @ state for state in yt]).flatten()
    
        # Tracé
        fig, axes = plt.subplots(3, 1, figsize=(8, 8), sharex=True)
    
        axes[0].plot(t, theta_t, color="tab:red", label=r"$\Delta \theta(t)$ (rad)")
        axes[0].axhline(0, color="grey", ls="--")
        axes[0].set_ylabel("Angle")
        axes[0].legend()
        axes[0].grid(True)
    
        axes[1].plot(t, phi_t, color="tab:green", label=r"$\Delta \phi(t)$ (rad)")
        axes[1].axhline(0, color="grey", ls="--")
        axes[1].set_ylabel("Commande")
        axes[1].legend()
        axes[1].grid(True)
    
        axes[2].plot(t, x_t, color="tab:blue", label=r"$\Delta x(t)$ (m)")
        axes[2].axhline(0, color="grey", ls="--")
        axes[2].set_xlabel("Temps $t$ (s)")
        axes[2].set_ylabel("Position")
        axes[2].legend()
        axes[2].grid(True)
    
        fig.suptitle("Pole Assignment Controller (Stabilité Asymptotique Complète)")
        fig.tight_layout()
        return fig

    simulate_pole_placement_controller()
    return (sig,)


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ## 🧩 Controller Tuned with Optimal Control

    Using optimal control, find a gain matrix $K_{oc}$ that satisfies the same set of requirements that the one defined using pole placement.

    Explain how you find the proper design parameters!
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ###

    **1. Principe de la Commande Optimale (LQR)**
    Plutôt que de deviner où placer les pôles, la commande optimale cherche à trouver la commande $u(t)$ (ici $\Delta \phi$) qui minimise une fonction de coût quadratique globale $J$ sur un horizon infini :
    $$J = \int_{0}^{+\infty} \left( \Delta s_{lat}(t)^T Q \Delta s_{lat}(t) + \Delta \phi(t)^T R \Delta \phi(t) \right) dt$$

    * $Q$ est une matrice (souvent diagonale) qui pénalise les écarts de l'état (position, inclinaison). Des valeurs élevées pour $Q$ forcent une convergence rapide vers zéro.
    * $R$ est une matrice (ici un scalaire car on a une seule entrée $\Delta \phi$) qui pénalise l'effort de commande. Une valeur élevée pour $R$ garantit que l'angle de la tuyère restera petit.

    **2. Résolution via l'Équation de Riccati**
    D'après le cours, la matrice de gain optimale est donnée par $K_{oc} = R^{-1}B_{lat}^T\Pi$, où $\Pi$ est la solution symétrique définie positive de l'Équation Algébrique de Riccati Continue (ARE) : $\Pi B_{lat} R^{-1} B_{lat}^T \Pi - \Pi A_{lat} - A_{lat}^T \Pi - Q = 0$.

    **3. Choix des paramètres de conception ($Q$ et $R$)**
    Puisque nous voulons ramener $x$ et $\theta$ à zéro en environ 20 secondes tout en gardant $\phi$ modéré :
    * Nous pénalisons fortement l'erreur de position $x$ et l'angle $\theta$ en choisissant $Q = \text{diag}(1, 1, 10, 1)$ (pour corriger agressivement l'inclinaison).
    * Nous fixons $R = [100]$ pour pénaliser fortement la commande et éviter que la tuyère ne dépasse les limites physiques (pour respecter $|\Delta \phi| < \pi/2$).
    *(Ces valeurs peuvent être ajustées itérativement pour affiner le temps de réponse).*
    """)
    return


@app.cell
def _(A_lat, B_lat, np):
    from scipy.linalg import solve_continuous_are

    def compute_optimal_controller():
    
        Q = np.diag([1.0, 1.0, 10.0, 1.0])
        R = np.array([[100.0]])
    
        # Résolution de l'équation algébrique de Riccati (ARE)
        Pi = solve_continuous_are(A_lat, B_lat, Q, R)
    
        # Calcul de la matrice de gain optimale K_oc
        K_oc = np.linalg.inv(R) @ B_lat.T @ Pi
    
        # Vérification de la stabilité de la boucle fermée
        A_cl_oc = A_lat - B_lat @ K_oc
        eig_oc = np.linalg.eigvals(A_cl_oc)
    
        print("Matrice de gain optimale K_oc :", np.round(K_oc, 3))
        print("Valeurs propres en boucle fermée :", np.round(eig_oc, 3))
    
        return K_oc

    K_oc = compute_optimal_controller()
    return (K_oc,)


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ## 🧩 Validation

    Test the two control strategies (pole placement and optimal control) on the "true" (nonlinear) model with an animation. Check that both controllers achieve their goal; otherwise, go back to the drawing board and tweak the design parameters until they do!
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ###

    Nous allons maintenant tester et comparer nos deux stratégies de contrôle (Placement de pôles $K_{pp}$ et Commande optimale $K_{oc}$) sur le **modèle non-linéaire complet**.

    Pour cela, nous réutilisons la structure `tilted_landing_law` définie dans le notebook, qui gère la trajectoire verticale planifiée (polynôme de degré 5) et y superpose le retour d'état latéral linéaire pour calculer l'angle $\phi$.

    Nous définissons la condition initiale exigeante de la section "Off-center" :
    * Décalage initial : $x_0 = 2.5$ m
    * Inclinaison initiale : $\theta_0 = 30^\circ$ ($\pi/6$)
    * Temps de simulation : $T = 5.0$ s (et on laisse déborder un peu pour voir la stabilisation à l'atterrissage si on le souhaite, bien que la trajectoire soit prévue sur 5s).

    Si les paramètres sont bien choisis, les deux animations montreront la fusée compenser son décalage latéral en s'inclinant, pour finir parfaitement droite et centrée sur la cible verte.
    """)
    return


@app.cell
def _(A_lat, B_lat, M, booster_anim, g, l, np, redstart_solve, sig, world):

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
            view_box, 
            booster_anim(x_t, y_t, theta_t, f_t, phi_t, T=T)
        )
    def optimal_landing_law(theta_0, K_matrix):

        T = 5.0
    
        a0_y, a1_y, a2_y = 10.0, -2.0, -g / 2.0
        A_y = np.array([
            [T**3, T**4, T**5],
            [3 * T**2, 4 * T**3, 5 * T**4],
            [6 * T, 12 * T**2, 20 * T**3],
        ])
        rhs_y = np.array([
            l - a0_y - a1_y * T - a2_y * T**2,
            0.0 - a1_y - 2 * a2_y * T,
            0.0 - 2 * a2_y,
        ])
        a3_y, a4_y, a5_y = np.linalg.solve(A_y, rhs_y)

        def y_ddot(t):
            return 2 * a2_y + 6 * a3_y * t + 12 * a4_y * t**2 + 20 * a5_y * t**3

        ALPHA_MAX = np.radians(85.0)

    
        def f_phi_law(t, s):
            if s is None:
                return np.array([M * (y_ddot(t) + g), 0.0])
        
            # Extraction de l'état latéral
            x_val, vx_val, theta_val, om_val = s[0], s[1], s[4], s[5]
        
            # Application du gain
            phi = float(-K_matrix[0, 0] * x_val - K_matrix[0, 1] * vx_val - K_matrix[0, 2] * theta_val - K_matrix[0, 3] * om_val)
        
        
            phi = float(np.clip(phi, -ALPHA_MAX - theta_val, ALPHA_MAX - theta_val))
            denom = np.cos(theta_val + phi)
        
            if abs(denom) < 1e-3:
                return np.array([0.0, 0.0])
            
            f = M * (y_ddot(t) + g) / denom
            if f < 0.0:
                f = 0.0
            
            return np.array([f, phi])

        return f_phi_law


    poles = [-1.2, -1.25, -1.3, -1.35]
    K_pp = sig.place_poles(A_lat, B_lat, poles).gain_matrix

    THETA_0_OFFSET = np.pi / 6
    X_0 = 2.5
    y0_validation = [X_0, 0.0, 10.0, -2.0, THETA_0_OFFSET, 0.0]



    return (
        K_pp,
        THETA_0_OFFSET,
        animate_scenario,
        optimal_landing_law,
        y0_validation,
    )


@app.cell
def _(
    K_oc,
    K_pp,
    THETA_0_OFFSET,
    animate_scenario,
    mo,
    optimal_landing_law,
    y0_validation,
):
    mo.md("### Validation : Placement de Pôles vs Commande Optimale")
    mo.hstack([
        mo.vstack([
            mo.md("**Pole Placement ($K_{pp}$)**").center(),
            mo.Html(animate_scenario(y0_validation, optimal_landing_law(THETA_0_OFFSET, K_pp)))
        ]),
        mo.vstack([
            mo.md("**Optimal Control ($K_{oc}$)**").center(),
            mo.Html(animate_scenario(y0_validation, optimal_landing_law(THETA_0_OFFSET, K_oc)))
        ])
    ], justify="space-around")
    return


if __name__ == "__main__":
    app.run()
