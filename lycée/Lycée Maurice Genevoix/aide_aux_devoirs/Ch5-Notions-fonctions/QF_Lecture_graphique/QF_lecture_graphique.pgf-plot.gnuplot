set table "QF_lecture_graphique.pgf-plot.table"; set format "%.5f"
set samples 100.0; set parametric; plot [t=0:1] [] [] -3*t+9*t^2-4*t^3,9*t^3-15*t^2+6*t
