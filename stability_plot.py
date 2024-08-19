
import json
import numpy as np


def parse_html(path: str):
    res = ""
    with open(path, "r") as file:
        lines = file.readlines()
        for line in lines[17:]:
            if "}" in line:
                break
            res += line
        res += "}"
    return res


def parse_files(files):
    all_values = []
    tables = ["" for file in files]

    for table, jsonstr in enumerate(files):
        data = json.loads(jsonstr)
        for i, k in enumerate(data["x"]):
            for j, lam in enumerate(data["y"]):
                val = np.log10(data["z"][j][i])
                all_values += [val]
                tables[table] += f"{k} {lam} {val}\n"
            tables[table] += "\n"

    minimum = np.floor(10*min(all_values))/10.
    maximum = np.ceil(10*max(all_values))/10.
    return tables, minimum, maximum


def get_levels(minimum, maximum):
    levels = ""
    for i in range(int(np.floor(minimum*2)), int(np.ceil(maximum*2))):
        levels += f"{int(i*0.5) if i%2==0 else i*0.5},"
    levels = "{" + levels[:-1] + "}"
    return levels


eossph = parse_html(
    "/home/julian/Code/stoked2d/analysis/plot_stability_int_k_lambda_SESPH_1723605466.html")
splitsph = parse_html(
    "/home/julian/Code/stoked2d/analysis/plot_stability_int_k_lambda_SplittingSESPH_1723609471.html")
itersph = parse_html(
    "/home/julian/Code/stoked2d/analysis/plot_stability_int_k_lambda_IterSESPH_1723619795.html")


eossph_vis = parse_html(
    "/home/julian/Code/stoked2d/analysis/plot_stability_int_k_nu_SESPH_1723603157.html")
splitsph_vis = parse_html(
    "/home/julian/Code/stoked2d/analysis/plot_stability_int_k_nu_SplittingSESPH_1723607502.html")
itersph_vis = parse_html(
    "/home/julian/Code/stoked2d/analysis/plot_stability_int_k_nu_IterSESPH_1723614769.html")


# FIRST FIGURE ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

tables, minimum, maximum = parse_files([eossph, splitsph, itersph])
levels = (get_levels(minimum, maximum))

result = r"""
\begin{figure}
  \centering
  \begin{subfigure}[t]{\textwidth}
    \centering
    \begin{tikzpicture}
      \begin{groupplot}[
          group style={
              group size=2 by 3,
              vertical sep=2cm,
              horizontal sep=2cm,
            },
          colormap name=Spectral_r,
          % colormap/viridis, 
          point meta min="""+str(minimum)+r""",
          point meta max="""+str(maximum)+r""",
          view={0}{90},
          xlabel={$k$},
          ylabel={$\lambda$},
          zlabel={$\epsilon$},
          width=0.45\textwidth,
          height=0.45\textwidth,
        ]
        \nextgroupplot[
          title={\texttt{EOSSPH}}
        ]

        \addplot3 [
          contour filled,
        ] table {"""+tables[0]+r"""};

        \addplot3 [
          contour gnuplot={
              contour dir=z,
              levels="""+levels+r""",
              labels over line,
              draw color = black,
            },
          thick,
        ] table {"""+tables[0]+r"""};
        \nextgroupplot[
          title={\texttt{EOSSPH}},
          view={60}{30},
          x dir=reverse,
          zmin="""+str(minimum)+r""",
          zmax="""+str(maximum)+r""",
          % zlabel={\Epsilon},
        ]
        \addplot3 [
          surf,
          faceted color=black,
        ] table {"""+tables[0]+r"""};

				% -----------------------------------------------------------------------------------------------
      
        \nextgroupplot[
          title={\texttt{SplitSPH}}
        ]
        \addplot3 [
          contour filled,
        ] table {"""+tables[1]+r"""};
        \addplot3 [
          contour gnuplot={
              contour dir=z,
              levels="""+levels+r""",
              labels over line,
              draw color = black,
            },
          thick,
        ] table {"""+tables[1]+r"""};
        \nextgroupplot[
          title={\texttt{SplitSPH}},
          view={60}{30},
          x dir=reverse,
          zmin="""+str(minimum)+r""",
          zmax="""+str(maximum)+r""",
          % zlabel={\Epsilon},
        ]
        \addplot3 [
          surf,
          faceted color=black,
        ] table {"""+tables[1]+r"""};

				% -----------------------------------------------------------------------------------------------
        
        \nextgroupplot[
          title={\texttt{IterSPH}}
        ]
        \addplot3 [
          contour filled,
        ] table {"""+tables[2]+r"""};

        \addplot3 [
          contour gnuplot={
              contour dir=z,
              levels="""+levels+r""",
              labels over line,
              draw color = black,
            },
          thick,
        ] table {"""+tables[2]+r"""};

        \nextgroupplot[
          title={\texttt{IterSPH}},
          view={60}{30},
          x dir=reverse,
          zmin="""+str(minimum)+r""",
          zmax="""+str(maximum)+r""",
          % zlabel={\Epsilon},
        ]
        \addplot3 [
          surf,
          faceted color=black,
        ] table {"""+tables[2]+r"""};
      \end{groupplot}
    \end{tikzpicture}

  \end{subfigure}
  \begin{subfigure}[t]{\textwidth}
    \centering
    \begin{tikzpicture}
      \begin{axis}[
          hide axis,
          scale only axis,
          height=0pt,
          width=0pt,
          colormap name=Spectral_r,
          colorbar horizontal,
          point meta min="""+str(minimum)+r""",
          point meta max="""+str(maximum)+r""",
          colorbar style={
              width=0.5\textwidth,
            }]
        \addplot [draw=none] coordinates {(0,0)};
      \end{axis}
    \end{tikzpicture}

  \end{subfigure}
  \caption*{\begin{tiny}$\nu=10^{-4}, \nu_2=10^{-3}, h=0.02, N=1572, \rho_0 = 1, \gamma_1=1, \gamma_2=0.5, l_{min}=5, l_{max}=300$, Hexagonal sampling with $\sigma=0.015h$\end{tiny}}
  \caption{The error $\epsilon$ (\autoref{eq:action-log-error}) in the kinetic energy of the resting water column is plotted for different parameters of time step size $\lambda\in[0,1]$ and stiffness $k\in[500,1500]$ for $5\times 5$ datapoints. Each row shows one solver, where the left column are contour plots and the right column shows the same values in 3D for better visual clarity. The mapping from values to colours is shown in the bar at the bottom.}
  \label{fig:stability-k-lambda}
\end{figure}
"""

with open("05b-figure-stability.tex", "w") as text_file:
    text_file.write(result)


# SECOND  FIGURE ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
tables, minimum_alt, maximum_alt = parse_files([eossph_vis, splitsph_vis])
levels = (get_levels(minimum, maximum))

result = r"""
\begin{figure}[hb]
  \centering
  \begin{subfigure}[t]{\textwidth}
    \centering
    \begin{tikzpicture}
      \begin{groupplot}[
          group style={
              group size=2 by 1,
              vertical sep=2cm,
              horizontal sep=2cm,
            },
          colormap name=Spectral_r,
          % colormap/viridis, 
          point meta min="""+str(minimum)+r""",
          point meta max="""+str(maximum)+r""",
          view={0}{90},
          xlabel={$k$},
          ylabel={$\nu$},
          zlabel={$\epsilon$},
          width=0.45\textwidth,
          height=0.45\textwidth,
        ]
        \nextgroupplot[
          title={\texttt{EOSSPH}}
        ]

        \addplot3 [
          contour filled,
        ] table {"""+tables[0]+r"""};

        \addplot3 [
          contour gnuplot={
              contour dir=z,
              levels="""+levels+r""",
              labels over line,
              draw color = black,
            },
          thick,
        ] table {"""+tables[0]+r"""};

				% -----------------------------------------------------------------------------------------------
      
        \nextgroupplot[
          title={\texttt{SplitSPH}}
        ]
        \addplot3 [
          contour filled,
        ] table {"""+tables[1]+r"""};
        \addplot3 [
          contour gnuplot={
              contour dir=z,
              levels="""+levels+r""",
              labels over line,
              draw color = black,
            },
          thick,
        ] table {"""+tables[1]+r"""};
      \end{groupplot}
    \end{tikzpicture}

  \end{subfigure}
  \caption*{\begin{tiny}$\lambda=0.1, \nu_2=10^{-3}, h=0.02, N=1572, \rho_0 = 1, \gamma_1=1, \gamma_2=0.5$, Hexagonal sampling with $\sigma=0.015h$\end{tiny}}
  \caption{The error $\epsilon$ (\autoref{eq:action-log-error}) is plotted for different parameters of time step size $\lambda\in[0,1]$ and viscosity $\nu\in[10^{-4}, 2\cdot10^{-3}]$ for $5\times 5$ datapoints. The mapping from values to colours is the same as in \autoref{fig:stability-k-lambda}.}
  \label{fig:stability-k-nu}
\end{figure}
"""

with open("05c-figure-stability-vis.tex", "w") as text_file:
    text_file.write(result)
