var
  i,x:integer;
  s:string;
  begin
    write('stroka:');
    read(s);
    for x:=1 to length(s) do begin
    if (s[x] >= '0') and (s[x] <= '9') then
      i+=1;
    end;
    write(i)
  end.
