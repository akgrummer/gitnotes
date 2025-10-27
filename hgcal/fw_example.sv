reg [2:0] refCtr;
always @(posedge clk100 or posedge reset_in) begin
    refCtr <= refCtr +1;
	end

