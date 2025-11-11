FROM mcr.microsoft.com/dotnet/sdk:8.0 AS build

WORKDIR /src
COPY MultiStage.csproj .
RUN dotnet restore
COPY . .

RUN dotnet build "MultiStage.csproj" -c Release -o /app/build

RUN dotnet publish -c Release -o /app

FROM mcr.microsoft.com/dotnet/sdk:8.0
WORKDIR /app
COPY --from=build /app . 
ENTRYPOINT [ "dotnet", "MultiStage.dll" ]