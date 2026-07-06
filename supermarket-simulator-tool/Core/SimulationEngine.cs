namespace SupermarketSimulatorTool.Core;

public class SimulationEngine : ISimulationEngine
{
    private CancellationTokenSource? _cts;
    private Task? _loopTask;
    private float _speedMultiplier = 1.0f;

    public bool IsRunning => _loopTask is { IsCompleted: false };
    public int CurrentTick { get; private set; }

    public void Start()
    {
        if (IsRunning) return;
        _cts = new CancellationTokenSource();
        var token = _cts.Token;
        _loopTask = Task.Run(async () =>
        {
            while (!token.IsCancellationRequested)
            {
                CurrentTick++;
                await Task.Delay((int)(1000 / _speedMultiplier), token);
            }
        }, token);
    }

    public void Stop()
    {
        _cts?.Cancel();
        _cts = null;
    }

    public void AdjustSpeed(float multiplier)
    {
        _speedMultiplier = Math.Clamp(multiplier, 0.1f, 10.0f);
    }
}