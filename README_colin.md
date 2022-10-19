# README - from Colin

Hi David - here are some notes on the submission.

## How to run:
> make build
> make run

Note that it runs the python server in the background, so you might have to kill that process if you want to rerun

## Improvements that I would make

### Frontend
- I would test more! I left in some stubbs, even though right now they are not useful. For instance, the current version of the table is so simple of a component that testing is not worthwhile. I would test the box behavior as well.
- I would use a proper CORS config instead of a proxy, but am running everything in dev so figured that was ok
- I'd probably integration test the api call, including failures and at least some mock data
- CSS could use an overhaul - right now I'm overriding the ViewEncapsulation so that I can have global styles easily. Also, it goes without saying that it looks... not very beautiful!
- I've checked in the secret key and the server is currently in dev mode, so definitely would change both of those before prod

### Backend
- I don't love the data model that I used in the sqllite database. I think I'd prefer to keep the 'FakeSolar' type of data model with the extra granularlity instead of the aggregated data for flexibility in the future. (i.e. instead of keeping the number of critical and warning issues, keep the details of the issues themselves)
- There is a note about which date we should use for the inspection in the solargrade/inspections/models.py file. I made a decision, but it's probably something that I'd chat with the team about before implementing to make sure it's properly capturing the business context.

### General
- Probably more type-checks everywhere: compile-time errors are better than runtime errors!
