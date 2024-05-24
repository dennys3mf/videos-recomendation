using System;
using System.Threading.Tasks;
using StackExchange.Redis;
using Npgsql;
using Confluent.Kafka;

class Program
{
    private static readonly string redisConnectionString = "redis:6379";
    private static readonly string postgresConnectionString = "Host=postgres;Username=postgres;Password=example;Database=videos";
    private static readonly string kafkaBroker = "kafka:9092";
    private static readonly string topic = "video_watched";

    static async Task Main(string[] args)
    {
        var redis = await ConnectionMultiplexer.ConnectAsync(redisConnectionString);
        var db = redis.GetDatabase();
        var consumerConfig = new ConsumerConfig
        {
            GroupId = "recommendation_service",
            BootstrapServers = kafkaBroker,
            AutoOffsetReset = AutoOffsetReset.Earliest
        };
        
        using var consumer = new ConsumerBuilder<Ignore, string>(consumerConfig).Build();
        consumer.Subscribe(topic);

        while (true)
        {
            var consumeResult = consumer.Consume();
            var message = consumeResult.Message.Value.Split(',');
            var userId = message[0];
            var videoId = message[1];
            await SaveWatchEventToPostgres(userId, videoId);
            // Implement recommendation logic here
        }
    }

    private static async Task SaveWatchEventToPostgres(string userId, string videoId)
    {
        await using var conn = new NpgsqlConnection(postgresConnectionString);
        await conn.OpenAsync();

        await using var cmd = new NpgsqlCommand("INSERT INTO watch_events (user_id, video_id) VALUES (@userId, @videoId)", conn);
        cmd.Parameters.AddWithValue("userId", userId);
        cmd.Parameters.AddWithValue("videoId", videoId);
        await cmd.ExecuteNonQueryAsync();
    }
}
