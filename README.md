# Uninformed Search Graph

## Graph

The graph look like this
<br>
[![](https://mermaid.ink/img/eyJjb2RlIjoiZ3JhcGggVERcbiAgICAxIC0tLSA0XG4gICAgMSAtLS0gMlxuICAgIDQgLS0tIDNcbiAgICAyIC0tLSAzXG4gICAgMyAtLS0gMTBcbiAgICAzIC0tLSA5XG4gICAgMiAtLS0gOFxuICAgIDggLS0tIDdcbiAgICAyIC0tLSA3XG4gICAgMiAtLS0gNVxuICAgIDUgLS0tIDZcbiAgICA1IC0tLSA3XG5cbiIsIm1lcm1haWQiOnsidGhlbWUiOiJkZWZhdWx0In0sInVwZGF0ZUVkaXRvciI6ZmFsc2UsImF1dG9TeW5jIjp0cnVlLCJ1cGRhdGVEaWFncmFtIjpmYWxzZX0)](https://mermaid-js.github.io/mermaid-live-editor/edit#eyJjb2RlIjoiZ3JhcGggVERcbiAgICAxIC0tLSA0XG4gICAgMSAtLS0gMlxuICAgIDQgLS0tIDNcbiAgICAyIC0tLSAzXG4gICAgMyAtLS0gMTBcbiAgICAzIC0tLSA5XG4gICAgMiAtLS0gOFxuICAgIDggLS0tIDdcbiAgICAyIC0tLSA3XG4gICAgMiAtLS0gNVxuICAgIDUgLS0tIDZcbiAgICA1IC0tLSA3XG5cbiIsIm1lcm1haWQiOiJ7XG4gIFwidGhlbWVcIjogXCJkZWZhdWx0XCJcbn0iLCJ1cGRhdGVFZGl0b3IiOmZhbHNlLCJhdXRvU3luYyI6dHJ1ZSwidXBkYXRlRGlhZ3JhbSI6ZmFsc2V9)

## Deep First Search (DSF)

Tree based on DFS can be like this
<br>
[![](https://mermaid.ink/img/eyJjb2RlIjoiZ3JhcGggVERcbiAgICAxIC0tLSA0XG4gICAgNCAtLS0gM1xuICAgIDMgLS0tIDEwXG4gICAgMyAtLS0gOSBcbiAgICAzIC0tLSAyXG4gICAgMiAtLS0gOFxuICAgIDggLS0tIDdcbiAgICA3IC0tLSA1XG4gICAgNSAtLS0gNiIsIm1lcm1haWQiOnsidGhlbWUiOiJkZWZhdWx0In0sInVwZGF0ZUVkaXRvciI6ZmFsc2UsImF1dG9TeW5jIjp0cnVlLCJ1cGRhdGVEaWFncmFtIjpmYWxzZX0)](https://mermaid-js.github.io/mermaid-live-editor/edit#eyJjb2RlIjoiZ3JhcGggVERcbiAgICAxIC0tLSA0XG4gICAgNCAtLS0gM1xuICAgIDMgLS0tIDEwXG4gICAgMyAtLS0gOSBcbiAgICAzIC0tLSAyXG4gICAgMiAtLS0gOFxuICAgIDggLS0tIDdcbiAgICA3IC0tLSA1XG4gICAgNSAtLS0gNiIsIm1lcm1haWQiOiJ7XG4gIFwidGhlbWVcIjogXCJkZWZhdWx0XCJcbn0iLCJ1cGRhdGVFZGl0b3IiOmZhbHNlLCJhdXRvU3luYyI6dHJ1ZSwidXBkYXRlRGlhZ3JhbSI6ZmFsc2V9)

so one of the result can be:

```
1 -> 4 -> 3 -> 10 -> 9 -> 2 -> 8 -> 7 -> 5 -> 6
```

## Breath First Search (BSF)

Tree based on BSF can be like this
<br>
[![](https://mermaid.ink/img/eyJjb2RlIjoiZ3JhcGggVERcbiAgICAxIC0tLSA0XG4gICAgMSAtLS0gMlxuICAgIDQgLS0tIDNcbiAgICAyIC0tLSA4XG4gICAgMiAtLS0gN1xuICAgIDIgLS0tIDVcbiAgICAzIC0tLSAxMFxuICAgIDMgLS0tIDlcbiAgICA1IC0tLSA2XG4iLCJtZXJtYWlkIjp7InRoZW1lIjoiZGVmYXVsdCJ9LCJ1cGRhdGVFZGl0b3IiOmZhbHNlLCJhdXRvU3luYyI6dHJ1ZSwidXBkYXRlRGlhZ3JhbSI6ZmFsc2V9)](https://mermaid-js.github.io/mermaid-live-editor/edit#eyJjb2RlIjoiZ3JhcGggVERcbiAgICAxIC0tLSA0XG4gICAgMSAtLS0gMlxuICAgIDQgLS0tIDNcbiAgICAyIC0tLSA4XG4gICAgMiAtLS0gN1xuICAgIDIgLS0tIDVcbiAgICAzIC0tLSAxMFxuICAgIDMgLS0tIDlcbiAgICA1IC0tLSA2XG4iLCJtZXJtYWlkIjoie1xuICBcInRoZW1lXCI6IFwiZGVmYXVsdFwiXG59IiwidXBkYXRlRWRpdG9yIjpmYWxzZSwiYXV0b1N5bmMiOnRydWUsInVwZGF0ZURpYWdyYW0iOmZhbHNlfQ)

so one of the result can be:

```
1 -> 4 -> 2 -> 3 -> 8 -> 7 -> 5 -> 9 -> 10 -> 6
```

## NOTES

Please understand that graph's nodes in some levels might not ordered due to using auto generation tools
