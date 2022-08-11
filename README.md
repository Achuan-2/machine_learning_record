# machine_learning_record
my record of  Machine Learning

$$
\begin{aligned}
\frac{\partial{e}}{\partial{w}_{11\_2}} &= \frac{\partial{e}}{\partial{a}_{1\_2}} \cdot \frac{\partial{a}_{1\_2}}{\partial{z}_{1\_2}} \cdot \frac{\partial{z}_{1\_2}}{\partial{w}_{11\_2}}\\  
\frac{\partial{e}}{\partial{w}_{21\_2}} &= \frac{\partial{e}}{\partial{a}_{1\_2}} \cdot \frac{\partial{a}_{1\_2}}{\partial{z}_{1\_2}} \cdot \frac{\partial{z}_{1\_2}}{\partial{w}_{21\_2}}\\  
\frac{\partial{e}}{\partial{b}_{1\_2}} &= \frac{\partial{e}}{\partial{a}_{1\_2}} \cdot \frac{\partial{a}_{1\_2}}{\partial{z}_{1\_2}} \cdot \frac{\partial{z}_{1\_2}}{\partial{b}_{1\_2}}\\  
\frac{\partial{e}}{\partial{w}_{11\_1}} &= \frac{\partial{e}}{\partial{a}_{1\_2}} \cdot \frac{\partial{a}_{1\_2}}{\partial{z}_{1\_2}} \cdot \frac{\partial{z}_{1\_2}}{\partial{a}_{1\_1}} \cdot \frac{\partial{a}_{1\_1}}{\partial{z}_{1\_1}} \cdot \frac{\partial{z}_{1\_1}}{\partial{w}_{11\_1}}\\  
\frac{\partial{e}}{\partial{b}_{1\_1}} &= \frac{\partial{e}}{\partial{a}_{1\_2}}  \cdot \frac {\partial{a}_{1\_2}}{\partial{z}_{1\_2}}  \cdot \frac {\partial{z}_{1\_2}}{\partial{a}_{1\_1}}  \cdot \frac {\partial{a}_{1\_1}}{\partial{z}_{1\_1}}  \cdot \frac {\partial{z}_{1\_1}}{\partial{b}_{1\_1}}\\  
\frac{\partial{e}}{\partial{w}_{12\_1}} &= \frac{\partial{e}}{\partial{a}_{1\_2}} \cdot \frac{\partial{a}_{1\_2}}{\partial{z}_{1\_2}} \cdot \frac{\partial{z}_{1\_2}}{\partial{a}_{1\_1}} \cdot \frac{\partial{a}_{2\_1}}{\partial{z}_{2\_1}} \cdot \frac{\partial{z}_{2\_1}}{\partial{w}_{12\_1}}\\  
\frac{\partial{e}}{\partial{b}_{2\_1}} &= \frac{\partial{e}}{\partial{a}_{1\_2}}  \cdot \frac {\partial{a}_{1\_2}}{\partial{z}_{1\_2}}  \cdot \frac {\partial{z}_{1\_2}}{\partial{a}_{1\_1}}  \cdot \frac {\partial{a}_{2\_1}}{\partial{z}_{2\_1}}  \cdot \frac {\partial{z}_{2\_1}}{\partial{b}_{2\_1}}
\end{aligned}
$$

$$
\begin{aligned}
w_{11\_2} &= w_{11\_2} - \alpha \cdot \frac{\partial{e}}{\partial{w}_{11\_2}} \\ 
w_{21\_2} &= w_{21\_2} - \alpha \cdot \frac{\partial{e}}{\partial{w}_{21\_2}} \\ 
b_{1\_2} &= b_{1\_2} - \alpha \cdot \frac{\partial{e}}{\partial{b}_{1\_2}} \\
w_{11\_1} &= w_{11\_1} - \alpha \cdot \frac{\partial{e}}{\partial{w}_{11\_1}} \\
b_{1\_1} &= b_{1\_1} - \alpha \cdot \frac{\partial{e}}{\partial{b}_{1\_1}} \\ 
w_{12\_1} &= w_{12\_1} - \alpha \cdot \frac{\partial{e}}{\partial{w}_{12\_1}} \\ 
b_{2\_1} &= b_{2\_1} - \alpha \cdot \frac{\partial{e}}{\partial{b}_{2\_1}} \\ 
\end{aligned}
$$
