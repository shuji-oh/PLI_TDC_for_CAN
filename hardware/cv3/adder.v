module adder (
    output Sum,
    output Co,
    input A,
    input B,
    input Ci
);

assign Sum = A ^ B ^ Ci;
assign Co = (A&&B || (A||B)&&Ci);

endmodule
