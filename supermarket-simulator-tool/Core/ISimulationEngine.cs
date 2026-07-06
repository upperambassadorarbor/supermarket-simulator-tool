namespace SupermarketSimulatorTool.Core;

public interface ISimulationEngine
{
    void Start();
    void Stop();
    void AdjustSpeed(float multiplier);
    bool IsRunning { get; }
    int CurrentTick { get; }
}