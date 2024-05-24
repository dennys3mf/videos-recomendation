FROM mcr.microsoft.com/dotnet/sdk:5.0
WORKDIR /app
COPY . .
RUN dotnet publish -c Release -o out
CMD ["dotnet", "out/RecommendationService.dll"]
