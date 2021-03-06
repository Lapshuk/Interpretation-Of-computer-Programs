create table parents as
  select "abraham" as parent, "barack" as child union
  select "abraham"          , "clinton"         union
  select "delano"           , "herbert"         union
  select "fillmore"         , "abraham"         union
  select "fillmore"         , "delano"          union
  select "fillmore"         , "grover"          union
  select "eisenhower"       , "fillmore";

create table dogs as
  select "abraham" as name, "long" as fur, 26 as height union
  select "barack"         , "short"      , 52           union
  select "clinton"        , "long"       , 47           union
  select "delano"         , "long"       , 46           union
  select "eisenhower"     , "short"      , 35           union
  select "fillmore"       , "curly"      , 32           union
  select "grover"         , "short"      , 28           union
  select "herbert"        , "curly"      , 31;

create table sizes as
  select "toy" as size, 24 as min, 28 as max union
  select "mini",        28,        35        union
  select "medium",      35,        45        union
  select "standard",    45,        60;

-------------------------------------------------------------
-- PLEASE DO NOT CHANGE ANY SQL STATEMENTS ABOVE THIS LINE --
-------------------------------------------------------------

-- The size of each dog
create table size_of_dogs as
  select a.name as name, b.size as size from dogs as a, sizes as b
  where b.min < a.height and a.height <= b.max;

-- All dogs with parents ordered by decreasing height of their parent
create table by_height as
  select child from parents, dogs
  where parent = name order by -height;

-- Sentences about siblings that are the same size
create table sentences as
  with 
    siblings(first, second) as (
      select a.child, b.child from parents as a, parents as b 
      where a.parent = b.parent and a.child > b.child )

  select second || ' and ' || first || ' are ' || a.size || ' siblings' 
  from siblings, size_of_dogs as a, size_of_dogs as b 
  where a.size = b.size and a.name = first and b.name = second;

-- Ways to stack 4 dogs to a height of at least 170, ordered by total height
create table stacks as
  with 
    dogs_stack(dogs, total_height, new_height, n) as (
      select name, height, height, 1 from dogs union
      select dogs || ', ' || name, total_height+height, height, n+1 
      from dogs_stack, dogs
      where new_height < height and n < 4)

  select dogs, total_height from dogs_stack
    where total_height >= 170 and n = 4 order by total_height;



-- non_parents is an optional, but recommended question
-- All non-parent relations ordered by height difference
create table non_parents as
  select "REPLACE THIS LINE WITH YOUR SOLUTION";

create table ints as
    with i(n) as (
        select 1 union
        select n+1 from i limit 100
    )
    select n from i;

create table divisors as
  with 
    div(num, divisor) as (
      select a.n, b.n from ints as a, ints as b where a.n%b.n = 0)
  select num, count(*) as divisor_count from div group by num;


create table primes as
    select num from divisors 
    where divisor_count = 2 and divisor_count != 1;
