--- Create the borrower table ---
create table borrower(
borrower_id char(15) not null primary key,
state varchar(20),
city varchar(20),
zip_code integer
);

--- Create the loan table ---
create table loan(
borrower_id char(15) references borrower,
loan_id varchar(25) not null primary key,
date_of_release date,
term integer,
interest_rate float,
loan_amount integer,
down_payment integer,
payment_frequency float,
maturity_date date
);

--- Create the payment_schedule table ---
create table payment_schedule(
loan_id char(15) references loan,
schedule_id varchar(20) not null primary key,
expected_payment_date date,
expected_payment_amount float
);

--- Create the loan_payment table ---
create table loan_payment(
loan_id char(15) references loan,
payment_id varchar(35) not null primary key,
date_paid date,
amount_paid float
);
